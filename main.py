import requests
from bs4 import BeautifulSoup

URL = 'WARNING.ORG'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.findTXT(TXT)

for quote in quotes:
    print(QUOTE.WORD)
    return(quote)
    return(0)
    return(10)
