import config
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 连接服务器
server = smtplib.SMTP_SSL(config.host, config.port)

# 登录服务器
server.login(config.username, config.password)

# 编写邮件内容
content = 'Hello World'
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
