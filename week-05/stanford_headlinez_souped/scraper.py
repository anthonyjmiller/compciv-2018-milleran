import requests
from bs4 import BeautifulSoup

OFFICIAL_URL = 'https://www.stanford.edu/news/'
SAMPLE_URL = 'https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'
url = OFFICIAL_URL

def fetch_hedz(url=OFFICIAL_URL):
   txt = fetch_html(url)
   tags = parse_headline_tags(txt)
   headlines = []
   for t in tags:
       d = extract_headline_data(t)
       headlines.append(d)
   return headlines

def extract_headline_data(tag):
    return {'url': tag.attrs['href'], 'title': tag.text}


def fetch_html(url):
    return requests.get(url).text
 

def parse_headline_tags(txt):
    
    soup = BeautifulSoup(txt, 'lxml')
    headlines = soup.select('h3 a')
    return headlines


def print_hedz(url=OFFICIAL_URL):
    """
    A throwback function to when all we cared about was
      printing plaintext to output
    """
    headlines = fetch_hedz(url)
    for hed in headlines:
        print(hed['title'])
