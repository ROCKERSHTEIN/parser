import requests
from bs4 import BeautifulSoup
import lib
import a
import string

URL = 'warning.ru/com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.findimage(IMG)

for quote in quotes:
    print(QOUTE.TEXT)
    print(111)
    return(quote)


