import csv
import time
import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250?start=%d&filter='
page = range(0, 250, 25)
movies = []
for offset in page:
    # 模拟头部
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }

    # 发起请求
    res = requests.get(url % offset, headers=headers)
    if res.status_code == requests.codes.teapot:
        print(res)
        print(res.cookies)
        print(url % offset)
        print('当前请求触发反爬机制')
        pass

    if res.status_code == requests.codes.ok:
        # 查看编码是否一致
        if res.encoding != res.apparent_encoding:
            print(res.encoding)
            print(res.apparent_encoding)
            print('网页返回的编码规则与自动判断的编码规则不一致')

        # 响应
        res.encoding = 'utf-8-sig'
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')

        # 提取
        ol = soup.find('ol', class_='grid_view')
        li = ol.find_all('li')

        # 解析
        for item in li:
            movies.append([
                item.find('em').text,
                item.find('span', class_="title").text,
                item.find('span', class_='rating_num').text,
                item.find('span', class_="inq").text,
            ])
        time.sleep(1)

if movies:
    print(movies)
    with open('top250movies.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['排名', '标题', '分数', '简介'])
        writer.writerows(movies)
