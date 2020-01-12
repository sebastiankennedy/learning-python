import requests
import json
import bs4
import random

headers = {
    'origin': 'https://www.xslou.com',
    'referer': 'https://www.xslou.com/login.php',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

# 创建会话
session = requests.Session()

# 判断是否存在 cookie
try:
    cookies_txt = open('cookies.txt', 'r')
    cookies_str = cookies_txt.read()
    cookies_dict = json.loads(cookies_str)
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    session.cookies = cookies
except FileNotFoundError:
    # 模拟登陆
    login_url = 'https://www.xslou.com/login.php?do=submit'
    login_data = {
        'username': 'sebastian',
        'password': 'Sebastian#2019',
        'usecookie': '86400',
        'action': 'login',
        'submit': ' 登  录 '
    }
    session.post(login_url, headers=headers, data=login_data)

    # 存储 cookie
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    cookies_str = json.dumps(cookies_dict)
    file = open('cookies.txt', 'w')
    file.write(cookies_str)
    file.close()

# 获取热门小说列表
top_url = 'https://www.xslou.com/top/allvisit_1/'
top_response = session.get(top_url, headers=headers)
if top_response.status_code != 200:
    print(top_response.status_code)
    print(top_response.text)

top_response.encoding = 'gb2312'
html = top_response.text
soup = bs4.BeautifulSoup(html, 'html.parser')

top_list = soup.find_all('ul', class_='update')
id_list = []
for top in top_list:
    link = top.find('a')['href']
    book_id = ''.join(list(filter(str.isdigit, link)))
    id_list.append(book_id)

# 从列表中随机获取一个编号进行推荐
book_id = random.choice(id_list)
recommend_url = 'https://www.xslou.com/modules/article/uservote.php?id=' + book_id
recommend_response = session.get(recommend_url, headers=headers)
recommend_response.encoding = 'gb2312'
print(recommend_response.status_code)
print(recommend_response.text)
