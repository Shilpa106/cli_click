from os import name
import click
from click.decorators import command


# # 1***********************************
import click
@click.command()
@click.option('-s','--string-to-echo')
def echo(string_to_echo):
    click.echo(string_to_echo)
echo()

# # 2*****************************************
@click.command()
@click.option('-s','--string-to-echo', 'string')
def echo(string):
    click.echo(string)

echo()

# # 3*******************make an option required***********************
@click.command()
@click.option('--n',default=1)
def dots(n):
    click.echo('.'*n)

dots()


# # 4**************# How to use a Python reserved word such as `from` as a parameter*******************************
@click.command()
@click.option('--from','-f','from_')
@click.option('--to','-t')
def reserved_param_name(from_,to):
    click.echo(f"from {from_} to {to}")

reserved_param_name()

# # 5*******************
@click.command()
@click.option('--n',default=1,show_default=True)
def dots(n):
    click.echo('.'*n)

dots()


# # *********************multivalue options**********
@click.command()
@click.option('--pos', nargs=2, type=float)
def findme(pos):
    a,b = pos
    click.echo(f"{a} / {b}")

findme()


# # **************************Tuples as Multi Value Options*******
@click.command()
@click.option('--item', type=(str, int))
def putitem(item):
    name, id=item
    click.echo(f"name={name} id={id}")
putitem()


# # **********************Multiple Options*****************
@click.command()
@click.option('--message', '-m', multiple=True)
@click.option("--format", multiple=True, default=["json"])
def commit(message):
    click.echo('\n'.join(message))

commit()

# # ***************************counting******************
@click.command()
@click.option('-v','--verbose', count=True)
def log(verbose):
    click.echo(f"Verbosity:{verbose}")
log()

# # **********************Boolean Flags*******************
import sys

@click.command()
@click.option('--shout/--no-shout', default=False)
def info(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper()+ '!!!!111'
    click.echo(rv)

info()

# # **********************************************
import sys

@click.command()
@click.option('--shout', is_flag=True)
def info(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!111'
    click.echo(rv)
info()


# # ********************************************
@click.command()
@click.option('/debug;/no-debug')
def log(debug):
    click.echo(f"debug={debug}")

if __name__ == '__main__':
    log()


# # ****************************
import sys

@click.command()
@click.option('--shout/--no-shout', ' /-S', default=False)
def info(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!111'
    click.echo(rv)
info()

# # ***************Feature Switches******************
import sys

@click.command()
@click.option('--upper', 'transformation', flag_value='upper',
              default=True)
@click.option('--lower', 'transformation', flag_value='lower')
def info(transformation):
    click.echo(getattr(sys.platform, transformation)())

info()

# # ******************Choice Options********************
@click.command()
@click.option('--hash-type',
              type=click.Choice(['MD5', 'SHA1'], case_sensitive=False))
def digest(hash_type):
    click.echo(hash_type)

digest()


# # ***********************Prompting**********************
@click.command()
@click.option('--name', prompt=True)
def hello(name):
    click.echo(f"Hello {name}!")

hello()

# # ***********************
@click.command()
@click.option('--name', prompt='Your name please')
def hello(name):
    click.echo(f"Hello {name}!")
hello()

# # *******************Password Prompts***************************
import codecs
@click.command()
@click.option(
    "--password", prompt=True, hide_input=True, confirmation_prompt=True)

def encode(password):
    click.echo(f"encoded: {codecs.encode(password, 'rot13')}")

encode()

# ********************
import codecs
@click.command()
@click.password_option()
def encrypt(password):
    click.echo(f"encoded: to {codecs.encode(password, 'rot13')}")

encrypt()


# # *************************Dynamic Defaults for Prompts******************

import os

@click.command()
@click.option(
    "--username", prompt=True,
    default=lambda: os.environ.get("USER", "")
)
def hello(username):
    click.echo(f"Hello , {username}!")


hello()

# # ********************
import os

@click.command()
@click.option(
     "--username", prompt=True,
    default=lambda: os.environ.get("USER", ""),
    show_default="current user"
)
def hello(username):
    click.echo(f"Hello, {username}!")

hello()


# # **************************Callbacks and Eager Options********
def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()

@click.command()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def hello():
    click.echo('Hello World!')

hello()

# # **********************Callback Signature Changes********
# ***Yes Parameters
def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()

@click.command()
@click.option('--yes', is_flag=True, callback=abort_if_false,
              expose_value=False,
              prompt='Are you sure you want to drop the db?')
def dropdb():
    click.echo('Dropped all tables!')

dropdb()


# # ****************************
@click.command()
@click.confirmation_option(prompt='Are you sure you want to drop the db?')
def dropdb():
    click.echo('Dropped all tables!')
dropdb()

# ******************Values from Environment Variables************
@click.command()
@click.option('--username')
def greet(username):
    click.echo(f'Hello {username}!')

if __name__=='__main__':
    greet(auto_envvar_prefix='GREETER')
