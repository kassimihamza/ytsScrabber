
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request(
    url='https://vw2.yts.vc/browse-movies/', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
html_page = urlopen(req).read()

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)