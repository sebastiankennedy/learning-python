import config
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

message = MIMEMultipart('mixed')
message['Subject'] = Header(config.subject)
message['From'] = Header(config.username163)
message['To'] = Header(config.receiver)
message['Cc'] = Header(config.other_receiver)
content = """\
<!doctype html>
<html>
<body>
    <p>
        各位同事：
    </p>
    <p>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这是我的工作日报，感谢你的阅读。
    </p>
    <p>
        工作内容如下：
    </p>
    <ul style="margin-left: 15px;">
        <li>不止心跳冒汗</li>
        <li>当然心跳冒汗</li>
        <li>忘了问你好吗</li>
        <li>应该怎么样说</li>
    </ul>
    <p>
        <img src="https://cdn.nlark.com/yuque/0/2019/png/168070/1574066473249-425f0a9e-b97e-4592-99c6-bc1ec57506b3.png" />
    </p>
</body>
</html>
"""

html = MIMEText(content, 'html', 'utf-8')
message.attach(html)
server = smtplib.SMTP_SSL(config.host163, config.port163)
try:
    server.login(config.username163, config.password163)
    server.sendmail(config.username163, config.receiver, message.as_string())
except Exception as e:
    print(e)
finally:
    server.quit()
