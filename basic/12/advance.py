class Robot:
    name = '瓦力'
    username = ''

    def __init__(self):
        self.username = input('你好，请问贵姓')
        print('你好，%s。我是%s。遇见你，真好。' % (self.username, self.name))

    def say_wish(self):
        content = input('请输出你的愿望')
        print(self.username + '的愿望是：')
        for i in range(0, 3):
            print(content)


robot = Robot()
robot.say_wish()
