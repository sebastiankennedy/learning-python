import requests
import bs4

res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
if res.status_code != 200:
    print('Something Wrong')

html = res.text
soup = bs4.BeautifulSoup(html, 'html.parser')

header_list = soup.find_all('header', class_='entry-header')
for header in header_list:
    print(header.find('time', class_='entry-date').text)
    print(header.find('h2', class_='entry-title').text)
    print(header.find('a')['href'])
