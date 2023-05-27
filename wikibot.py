import click
from mylib.bot import scrape

@click.command()
@click.option('--name',
              help='web page to scrape')
@click.option('--length',
            help='length of output')             
def cli(name,length):
    result= scrape(name,length)
    click.echo(click.style(f"{result}", bg="blue",fg="red"))

if __name__ == '__main__':
    cli()