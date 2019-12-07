# 需要的变量放到开头，明显一些。
choice = []
times = 0

while True:
    a = input('A，你认罪吗？请回答认罪或者不认：')
    b = input('B，你认罪吗？请回答认罪或者不认：')
    # 需要将每一对实验者的选择存起来。
    choice.append([a, b])
    times = times + 1

    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')
    elif a == '不认' and b == '认罪':
        print('A判20年，B判1年，唉')
    elif a == '认罪' and b == '不认':
        print('A判1年，B判20年')
    else:
        print('都判3年，太棒了')
        break

# 打印是第几对实验者做出了最优选择。
print('是第 %d 对实验者做出了最优选择' % times)

# 通过循环打印每一对实验者的选择。
j = 0
for i in choice:
    print('第 %d 次，A 的选择是 %s，B 的选择是 %s' % (j + 1, i[0], i[1]))
