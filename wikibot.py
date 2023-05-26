import wikipedia
import click

@click.command()
@click.option('--name', prompt='Wikipedia page to scrape',
              help='web page to scrape')
def scrape(name="microsoft",length=1):
    result= wikipedia.summary(name, sentences=length)
    click.echo(click.style(f"{result}", bg="blue",fg="red"))

if __name__ == '__main__':
    scrape('microsoft')