import requests 
from bs4 import BeautifulSoup 

url = 'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B4%D1%80%D0%BE%D0%B3%D0%BE%D0%B1%D0%B8%D1%87'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='tabs')


for item in items:
    print(item.text)