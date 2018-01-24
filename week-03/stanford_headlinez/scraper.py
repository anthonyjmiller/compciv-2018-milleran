def print_hedz(url='https://compciv.github.io/stash/hello.html'):
   txt = fetch_html(url)
   htags = parse_headline_tags(txt)
   for t in htags:
        hedtxt = extract_headline_text(t)
        print(hedtxt)

def extract_headline_text(txt):
    return txt.split('>')[2].split('<')[0]

def parse_headline_tags(url):
   mylist = []
   fulltext = html_fetch()
   lines = fulltext.splitlines()
   for line in lines:
      if '<h3><a' in line:
         mylist.append(line)
         return mylist

def fetch_html(url):
   import requests
   url = 'https://compciv.github.io/stash/hello.html'
   resp=requests.get(url)
   return(resp.text)
