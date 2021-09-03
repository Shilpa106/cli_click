# import click


# # 1*****************************************************
import click
@click.command()
def hello():
    click.echo('Hello world!')

if __name__=='__main__':
    hello()


# 2*******************************Nesting commands******************************
@click.group()
def cli():
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)

if __name__ == '__main__':
    cli()


# *********************************Registering Commands Later**********
@click.command()
def greet():
    click.echo("hello , world!")

@click.group()
def group():
    pass
group.add_command(greet)


# *****************************Adding Parameters*************
@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")

hello()