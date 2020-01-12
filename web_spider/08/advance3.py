import requests
import json

url = 'http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do'
headers = {
    'Host': 'ictclas.nlpir.org',
    'Origin': 'http://ictclas.nlpir.org',
    'Referer': 'http://ictclas.nlpir.org/nlpir/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
payload = {
    'content': '喜大同奔'
}

response = requests.post(url, headers=headers, data=payload)
if response.status_code != 200:
    print(response.status_code)

dict_data = json.loads(response.text)
list_data = dict_data['vjson']['v0']
for item in list_data:
    print(item)
