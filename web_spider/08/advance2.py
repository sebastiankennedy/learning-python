import requests
import json

url = 'http://openapi.tuling123.com/openapi/api/v2'
headers = {
    'content-type': 'charset=utf8'
}
payload = {
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": input('请输入您要发送的文本：')
        },
    },
    "userInfo": {
        "apiKey": "3915b0d3279f499eb401d8f65ff792c9",
        "userId": "546597"
    }
}
payload = json.dumps(payload)

response = requests.post(url, data=payload, headers=headers)
print(response.text)
