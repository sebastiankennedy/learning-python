import requests

url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md'
res = requests.get(url)
if res.status_code == 200:
    print(res.text)

url = 'https://res.pandateacher.com/2019-01-12-15-29-33.png'
img = requests.get(url)
if img.status_code == 200:
    with open('test.png', 'wb') as imgFile:
        imgFile.write(img.content)
