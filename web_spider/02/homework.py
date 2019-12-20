import requests
from bs4 import BeautifulSoup

url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/'
res = requests.get(url)

if res.status_code == 200:
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li', class_='comment')
    for item in items:
        print(item)
