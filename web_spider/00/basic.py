import requests

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
print(type(res))
# 响应码
print(res.status_code)
# 响应内容二进制格式
print(res.content)
# 响应内容文本格式
print(res.text)
# 响应内容编码模式
print(res.encoding)

# 发出请求，并把返回的结果放在变量 res 中
res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
# 把 Response 对象的内容以二进制数据的形式返回
picture = res.content
# 新建了一个文件 PPT.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
# 图片内容需要以二进制 wb 读写。你在学习 open() 函数时接触过它。
photo = open('ppt.jpg', 'wb')
# 获取 picture 的二进制内容
photo.write(picture)
# 关闭文件
photo.close()
