# 快递 100 查询
import requests
import random

no = input('请输入您要查询的快递单号：')
name = input('请输入您要查询的快递公司：')

url = 'https://www.kuaidi100.com/query'

params = {
    'type': name,
    'postid': no,
    'temp': '0.' + str(random.randrange(1111111111111111, 9999999999999999)),
    'phone': ''
}

headers = {
    'Host': 'www.kuaidi100.com',
    'Referer': 'https://www.kuaidi100.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

response = requests.get(url, params=params, headers=headers)
json = response.json()
print('请求连接：' + response.url)
print('请求状态：' + str(response.status_code))
print('请求内容：' + str(json))
for key, value in json.items():
    print(key, value)
