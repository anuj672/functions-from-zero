import fire
from mylib.bot import scrape

def hello(name="World"):
    return "hello %s!" % name

if __name__ == '__main__':
    fire.Fire(scrape)