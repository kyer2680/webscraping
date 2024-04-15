import requests
from bs4 import BeautifulSoup

tuckahoe_scrape = request.get()
soup = BeautifulSoup(tuckahoe_scrape.text, "html.parser")
links = soup.find_all("a"

for link in links