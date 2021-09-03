import click

@click.command()
@click.argument('number1',type=int)
@click.argument('number2',type=int)
@click.argument('method',default='add')


def main(number1,number2,method):
	""" Add Number 1 and Number 2"""
	if method == 'add':
		result = number1 + number2
	elif method == 'substract':
		result = number1 - number2
	elif method == 'multiply':
		result = number1 * number2
	click.echo(result)

# Multiple Argument - Variadic Arguments
@click.command()
@click.argument('source',nargs=-1)
@click.argument('destination',nargs=1)

def main(source,destination):
	for f in source:
		click.echo('Moving {} to Folder {}'.format(f,destination))



if __name__ == '__main__':
	main()
# 1*****************************************************************
import click

@click.command()
def cli():
    print("hello world")
cli()

# 2**********************************************************
import click

@click.group()
def main():
    pass

@main.command()
@click.argument("x", type=float)
@click.argument("y", type=float)
def add (x, y):
    print("%s + %s = %s" % (x, y, x+y))


@main.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def sub (x, y):
    print("%s - %s = %s" % (x, y, x-y))


@main.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def mul (x, y):
    print("%s * %s = %s" % (x, y, x*y))


@main.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def div (x, y):
    print("%s / %s = %s" % (x, y, x/y))


@main.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def mod (x, y):
    print("%s % %s = %s" % (x, y, x%y))

@main.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def pow (x, y):
    print("%s ** %s = %s" % (x, y, x**y))




if __name__=='__main__':
    main()




# 3******************************************************************************
import click



@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
def cli(verbose):
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello World")

cli()

# #4 ******************************************************************
import click

@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--name', default='', help='Who are you?')
def cli(verbose,name):
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello World")
    click.echo('Bye {0}'.format(name))

cli()

# # 5**********************************************************************
import click

@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--name', '-n', multiple=True, default='', help='Who are you?')
def cli(verbose,name):
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello World")
    for n in name:
        click.echo('Bye {0}'.format(n))

cli()

# #6 ******************************************************************************
import click

@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--name', '-n', multiple=True, default='', help='Who are you?')
def cli(verbose,name):
    """This is an example script to learn Click."""
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello World")
    for n in name:
        click.echo('Bye {0}'.format(n))

cli()

# 7**********************************************************************************
import click

@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--name', '-n', multiple=True, default='', help='Who are you?')
@click.password_option()
def cli(verbose,name, password):
    """This is an example script to learn Click."""
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello World")
    for n in name:
        click.echo('Bye {0}'.format(n))
    click.echo('We received {0} as password.'.format(password))


cli()

# 8****************************************************************
