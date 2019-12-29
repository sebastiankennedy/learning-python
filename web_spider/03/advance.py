import re
import bs4
import time
import requests
import urllib.request

search_list = []
ftp_link_list = []
magnet_link_list = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}

while True:
    string = input('请输入您想要观看的电影，停止搜索请输入 #：')
    if string == '#':
        print('已为您结束此进程')
        break

    movie = string.encode('gbk')
    search_url = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword=%s' % urllib.request.quote(movie)
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        print('Something Wrong')

    response.encoding = 'gb2312'
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')

    table_list = soup.find_all('table')
    table_list.pop(0)
    if not table_list:
        print('没有查询到相关电影')

    for table in table_list:
        a = table.find('a')
        search_list.append(a.text)
        print(a.text)
        time.sleep(1)

        detail_url = 'https://www.ygdy8.com/' + a['href']
        res = requests.get(detail_url, headers=headers)
        if response.status_code != 200:
            print('Something Wrong')
            continue

        res.encoding = 'gb2312'
        html = res.text
        soup = bs4.BeautifulSoup(html, 'html.parser')

        # 获取磁力下载链接
        magnet_link = soup.find('a', href=re.compile('magnet:?'))
        if hasattr(magnet_link, 'href'):
            magnet_link_list.append(magnet_link['href'])
            print(magnet_link['href'])

        ftp_link = soup.find('a', string=re.compile('ftp'))
        if hasattr(ftp_link, 'href'):
            ftp_link_list.append(ftp_link['href'])
            print(ftp_link['href'])
