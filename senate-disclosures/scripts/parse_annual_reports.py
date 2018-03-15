from pathlib import Path
from bs4 import BeautifulSoup

SRC_FILEPATH = Path('samples', 'grassley-report.html')

soup = BeautifulSoup(SRC_FILEPATH.read_text(), 'lxml')

sections = soup.select('section')

assets = sections[2]

