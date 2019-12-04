string = input('小精灵：您好，欢迎来到古灵阁，请问您需要帮助吗？需要or不需要？')
if string == '需要':
    number = int(input('小精灵：请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询'))

    if number == 1:
        print('小精灵：推荐你去存取款窗口')
    elif number == 3:
        print('小精灵：推荐你去咨询窗口')
    elif number == 2:
        print('小精灵：金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        money = float(input('小精灵：请问您需要兑换多少金加隆呢？'))
        print('小精灵：好的，我知道了，您需要兑换（你说的数字%f）金加隆。' % money)
        rmb = money * 51.3
        print('小精灵：那么，您需要付给我（你说的数字 %f）人民币。' % rmb)
else:
    print('小精灵：好的，再见。')
