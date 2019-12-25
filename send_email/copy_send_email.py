import time
import config
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 连接服务器
server = smtplib.SMTP_SSL(config.host)
server.connect(config.host, config.port)

# 登录服务器
server.login(config.username, config.password)

# 编写邮件内容
content = """
你好，世界。这是一封由 Python 程序群发的邮件。

当然心跳冒汗，
不止心跳冒汗。
"""
content_type = 'plain'
charset = 'utf-8'
content = MIMEText(content, content_type, charset)

# 指定发送者和接收人
sender = config.from_addr
receivers = config.to_addrs

# 编写邮件头部
date_time = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))
content['Subject'] = Header(config.subject + date_time, charset)
content['From'] = Header(sender)
content['To'] = Header(config.to_addr)
content['Cc'] = Header(','.join(config.to_addrs))

# 发送邮件
server.sendmail(sender, receivers, content.as_string())
server.quit()

print('发送人：' + sender)
print('接收人：' + config.to_addr)
print('抄送人：' + ','.join(config.to_addrs))
