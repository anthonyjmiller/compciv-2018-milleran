def print_hedz(url='https://www.stanford.edu/news/'):
txt = fetch_html(url)
    htags = parse_headline_tags(txt)

    for t in htags:
        hedtxt = extract_headline_text(t)
        print(hedtxt)

def extract_headline_text(txt):
    a = txt.split('<')[2]
    b = a.split('>')[1]
    return b

def parse_headline_tags(txt):
    hedtags = []
    lines = txt.splitlines()
        fulltext = html_fetch()
        lines = fulltext.splitlines()
        for line in lines:
        if HEADLINE_PATTERN in line:
            hedtags.append(line)
    return hedtags

def fetch_html(url):
 import requests
   url = 'https://compciv.github.io/stash/hello.html'
   resp=requests.get(url)
   return(resp.text)
