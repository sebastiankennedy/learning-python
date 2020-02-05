# 从 gevent 库里导入 monkey 模块
from gevent import monkey

# 把程序变成协作式运行
monkey.patch_all()

# 记录网站爬取所需时间
import time

# 实现多协程
import gevent

# 实现网站爬取
import requests

# 记录程序开始时间
start = time.time()

# 网站列表
url_list = ['https://www.baidu.com/',
            'https://www.sina.com.cn/',
            'http://www.sohu.com/',
            'https://www.qq.com/',
            'https://www.163.com/',
            'http://www.iqiyi.com/',
            'https://www.tmall.com/',
            'http://www.ifeng.com/']


# 定义一个 crawler() 函数
def crawler(url):
    response = requests.get(url)
    print(url, time.time() - start, response.status_code)


# 创建空的任务列表
tasks_list = []

for url in url_list:
    # 用 gevent.spawn() 函数创建任务
    task = gevent.spawn(crawler, url)
    # 往任务列表添加任务
    tasks_list.append(task)

# 执行所有任务
gevent.joinall(tasks_list)
print(time.time() - start)
