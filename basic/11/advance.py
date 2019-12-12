# 请你改造下面的代码，目标：不论输入了什么，程序都不会因报错而停止（即找到所有的报错类型）。

while True:
    print('\n欢迎使用除法计算器！\n')

    x = input('请你输入被除数：')
    y = input('请你输入除数：')

    try:
        z = float(x) / float(y)
        print(x, '/', y, '=', z)
        break
    except BaseException:
        print('SomeThing Wrong.')
