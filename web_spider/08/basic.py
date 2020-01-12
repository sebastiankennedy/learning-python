import requests

# 登录网址
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

# 登录参数
data = {
    'log': 'sebastiankennedy@foxmail.com',
    'pwd': 'Sebastian#2019',
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': 1
}

# 模拟登陆
response = requests.post(url, headers=headers, data=data)
if response.status_code != 200:
    print('模拟登陆失败')
    exit(0)

# 获取 cookies
cookies = response.cookies
comment_url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data = {
    'comment': 'Sebastian Kennedy 模拟登陆发表评论 - 超级棒棒',
    'submit': '发表评论',
    'comment_post_ID': '23',
    'comment_parent': '0'
}

# 提交评论
comment = requests.post(comment_url, headers=headers, data=data, cookies=cookies)
if comment.status_code != 200:
    print('提交评论失败')
    print(comment.status_code)
    print(comment.text)
else:
    print('提交评论成功')
