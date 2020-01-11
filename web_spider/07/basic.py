import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/people/zhang-jia-wei/posts/posts_by_votes?page=1'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
h2 = soup.find_all('h2', class_='ContentItem-title')

print(response.status_code)
print(h2)
