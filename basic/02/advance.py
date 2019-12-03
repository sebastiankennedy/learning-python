number = int(input('请输入您的工资：'))
if number:
    if number <= 500:
        print("欢迎进入史塔克穷人帮前三名")
        if 100 <= number <= 500:
            print('请找弗瑞队长加薪')
        else:
            print('恭喜您荣获“美元队长”称号！')
    elif 500 < number <= 1000:
        print('祝贺您至少可以温饱了。')
    elif number > 1000:
        print('经济危机都难不倒您！')
        if 1000 < number < 20000:
            print('您快比钢铁侠有钱了！')
        else:
            print('您是不是来自于瓦坎达国？')
else:
    print('输入数据类型错误')

print('程序结束')
