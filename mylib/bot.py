import wikipedia
def scrape(name="microsoft",length=1):
    result= wikipedia.summary(name, sentences=length)
    return result