import requests 
from bs4 import BeautifulSoup 

place = input("Введіть ваше місто ")
url = 'https://ua.sinoptik.ua/погода-' + str(place)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

today_time = soup.find_all('p', class_='today-time')
today_temp = soup.find_all('p', class_='today-temp')
prediction = soup.find_all('div', class_='description')

for _ in today_time:
    print(_.text)
for i in today_temp:
    print(i.text)
for i in prediction:
    print(i.text)





