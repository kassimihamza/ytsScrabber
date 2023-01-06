from unicodedata import name
import requests
page = requests.get("https://vw2.yts.vc/movie/hellraiser-2022/")

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


print(soup.find(attrs={'itemprop':'name'}).getText())
print(soup.find(href=True,attrs={'class':'magnet-download download-torrent magnet'})['href'])
