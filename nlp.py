import click
@click.group()
@click.version_option(version='0.01',prog_name='NLPiffy CLI')
def main():
    pass

@main.command()
@click.argument('text')
def tokens(text):
    click.echo(text)





if __name__=='__main__':
    main()