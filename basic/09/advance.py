import random
import time


def whoIsLuckyGay(params):
    a = random.choice(params)
    print('开奖倒计时', 3)
    time.sleep(1)
    print('开奖倒计时', 2)
    time.sleep(1)
    print('开奖倒计时', 1)
    time.sleep(1)
    image = '''
     /\_)o<
    |      \\
    | O . O|
     \_____/
    '''
    print(image)
    print('恭喜' + a + '中奖！')


luckyList = ['海绵宝宝', '派大星', '章鱼哥']
whoIsLuckyGay(luckyList)
