import requests
from bs4 import BeautifulSoup
import lib

URL = 'warning.ru/com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.findimage(IMG)

for quote in quotes:
    print(QOUTE.TEXT)
    return(quote)

