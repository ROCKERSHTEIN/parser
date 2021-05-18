import requests
from bs4 import BeautifulSoup

url = 'https://духи.рф/catalog/women'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('a', class_='items')

for quote in quotes:
    print(quote.text)
    return(quote)