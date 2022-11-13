import requests
from bs4 import BeautifulSoup

#파이어베이스 연동
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


undergraduate_schedule = []
graduate_schedule = []

undergraduate_schedule_date = []
graduate_schedule_date = []

url = 'https://www.chungbuk.ac.kr/site/www/sub.do?key=1853'
headers = {'User->Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
res = requests.get(url, headers)
soup = BeautifulSoup(res.content, 'lxml')

data = soup.select('div.schedule')

i = 0
for item in data:
    str[i] = item.get_text()
    i = i + 1
    
for i in len(str):
    print(str[i])
