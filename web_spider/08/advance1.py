import json
from tkinter import Tk, Button, Label, Text, END

import requests


class YouDaoFanyi(object):
    def __init__(self):
        pass

    def crawl(self, word):
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        # 使用post需要一个链接
        data = {'i': word,
                'from': 'AUTO',
                'to': 'AUTO',
                'smartresult': 'dict',
                'client': 'fanyideskweb',
                'doctype': 'json',
                'version': '2.1',
                'keyfrom': 'fanyi.web',
                'action': 'FY_BY_REALTIME',
                'typoResult': 'false'}
        # 将需要post的内容，以字典的形式记录在data内。
        r = requests.post(url, data)
        # post需要输入两个参数，一个是刚才的链接，一个是data，返回的是一个Response对象
        answer = json.loads(r.text)
        # 你可以自己尝试print一下r.text的内容，然后再阅读下面的代码。
        result = answer['translateResult'][0][0]['tgt']
        return result


class Application(object):
    def __init__(self):
        self.window = Tk()
        self.fanyi = YouDaoFanyi()

        self.window.title(u'我的翻译')
        # 设置窗口大小和位置
        self.window.geometry('310x370+500+300')
        self.window.minsize(310, 370)
        self.window.maxsize(310, 370)
        # 创建一个文本框
        # self.entry = Entry(self.window)
        # self.entry.place(x=10,y=10,width=200,height=25)
        # self.entry.bind("<Key-Return>",self.submit1)
        self.result_text1 = Text(self.window, background='azure')
        # 喜欢什么背景色就在这里面找哦，但是有色差，得多试试：http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
        self.result_text1.place(x=10, y=5, width=285, height=155)
        self.result_text1.bind("<Key-Return>", self.submit1)

        # 创建一个按钮
        # 为按钮添加事件
        self.submit_btn = Button(self.window, text=u'翻译', command=self.submit)
        self.submit_btn.place(x=205, y=165, width=35, height=25)
        self.submit_btn2 = Button(self.window, text=u'清空', command=self.clean)
        self.submit_btn2.place(x=250, y=165, width=35, height=25)

        # 翻译结果标题
        self.title_label = Label(self.window, text=u'翻译结果:')
        self.title_label.place(x=10, y=165)
        # 翻译结果

        self.result_text = Text(self.window, background='light cyan')
        self.result_text.place(x=10, y=190, width=285, height=165)
        # 回车翻译

    def submit1(self, event):
        # 从输入框获取用户输入的值
        content = self.result_text1.get(0.0, END).strip().replace("\n", " ")
        # 把这个值传送给服务器进行翻译

        result = self.fanyi.crawl(content)
        # 将结果显示在窗口中的文本框中

        self.result_text.delete(0.0, END)
        self.result_text.insert(END, result)

        # print(content)

    def submit(self):
        # 从输入框获取用户输入的值
        content = self.result_text1.get(0.0, END).strip().replace("\n", " ")
        # 把这个值传送给服务器进行翻译

        result = self.fanyi.crawl(content)
        # 将结果显示在窗口中的文本框中

        self.result_text.delete(0.0, END)
        self.result_text.insert(END, result)
        print(content)

    # 清空文本域中的内容
    def clean(self):
        self.result_text1.delete(0.0, END)
        self.result_text.delete(0.0, END)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()
