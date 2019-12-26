import requests

response = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
print(response.status_code)

if response.status_code == 200:
    with open('demo.mp3', 'wb') as mp3:
        mp3.write(response.content)