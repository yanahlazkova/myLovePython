import requests
from bs4 import BeautifulSoup

link = 'https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BF%D1%80%D0%B5%D0%B7%D0%B8%D0%B4%D0%B5%D0%BD%D1%82%D1%96%D0%B2_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8'
responce = requests.get(link).text
# print(responce)

soup = BeautifulSoup(responce, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'}).find_all('tr')


for item in range(2, len(table)):

    prezident = table[item].find_all_next('a')[2].text

    print(prezident)
