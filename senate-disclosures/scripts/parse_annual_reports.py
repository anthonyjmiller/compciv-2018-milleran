from pathlib import Path
from bs4 import BeautifulSoup

SRC_FILEPATH = Path('samples', 'gardner-2016-annual-report.html')

soup = BeautifulSoup(SRC_FILEPATH.read_text(), 'lxml')

sections = soup.select('section')

assets = sections[2]

