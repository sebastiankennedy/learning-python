import requests
import config
import smtplib
import schedule
from bs4 import BeautifulSoup
from email.header import Header
from email.mime.text import MIMEText


def send_menu():
    res_foods = requests.get('http://www.xiachufang.com/explore/')
    bs_foods = BeautifulSoup(res_foods.text, 'html.parser')
    list_foods = bs_foods.find_all('div', class_='info pure-u')

    foods = []

    for food in list_foods:
        tag_a = food.find('a')
        name = tag_a.text[17:-13]
        URL = 'http://www.xiachufang.com' + tag_a['href']
        tag_p = food.find('p', class_='ing ellipsis')
        ingredients = tag_p.text[1:-1]
        foods.append([name, URL, ingredients])

    # 连接服务器
    server = smtplib.SMTP_SSL(config.host, config.port)

    # 登录服务器
    server.login(config.username, config.password)

    # 编写邮件内容
    content = ''
    for food in foods:
        content += food[0] + food[1] + food[2] + "\n"

    content_type = 'plain'
    charset = 'utf-8'
    content = MIMEText(content, content_type, charset)

    # 编写邮件头部
    content['From'] = config.from_addr
    content['To'] = config.to_addr
    content['Subject'] = Header(config.subject, charset)

    # 发送邮件
    server.sendmail(config.from_addr, config.to_addr, content.as_string())
    server.quit()


# 部署每周一执行 send_menu 函数
schedule.every().monday.do(send_menu)

# 执行定时任务
schedule.run_pending()
