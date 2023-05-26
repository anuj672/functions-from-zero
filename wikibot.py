import click
from mylib.bot import scrape

@click.command()
@click.option('--name', prompt='Wikipedia page to scrape',
              help='web page to scrape')
def cli(name="microsoft",length=1):
    result= scrape(name, sentences=length)
    click.echo(click.style(f"{result}", bg="blue",fg="red"))

if __name__ == '__main__':
    cli()