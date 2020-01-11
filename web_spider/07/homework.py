import requests

link = requests.get('https://www.shanbay.com/api/v1/vocabtest/category/')
js_link = link.json()
bianhao = int(input('''请输入你选择的词库编号，按Enter确认
1，GMAT  2，考研  3，高考  4，四级  5，六级
6，英专  7，托福  8，GRE  9，雅思  10，任意
>'''))

ciku = js_link['data'][bianhao - 1][0]
test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=' + ciku)
words = test.json()
danci = []
words_knows = []
not_knows = []
print('测试现在开始。如果你认识这个单词，请输入Y，否则直接敲Enter：')
n = 0
for x in words['data']:
    n = n + 1
    print("\n第" + str(n) + '个：' + x['content'])
    answer = input('认识请敲Y，否则敲Enter：')
    if answer == 'Y':
        danci.append(x['content'])
        words_knows.append(x)
    else:
        not_knows.append(x)

print('\n在上述' + str(len(words['data'])) + '个单词当中，有' + str(len(danci)) + '个是你觉得自己认识的，它们是：')
print(danci)

print('现在我们来检测一下，你有没有真正掌握它们：')
wrong_words = []
right_num = 0
for y in words_knows:
    print('\n\n' + 'A:' + y['definition_choices'][0]['definition'])
    print('B:' + y['definition_choices'][1]['definition'])
    print('C:' + y['definition_choices'][2]['definition'])
    print('D:' + y['definition_choices'][3]['definition'])
    xuanze = input('请选择单词\"' + y['content'] + '\"的正确翻译（输入字母即可）：')
    dic = {'A': y['definition_choices'][0]['rank'], 'B': y['definition_choices'][1]['rank'],
           'C': y['definition_choices'][2]['rank'], 'D': y['definition_choices'][3]['rank']}
    if dic[xuanze] == y['rank']:
        right_num += 1
    else:
        wrong_words.append(y)

print('现在，到了公布成绩的时刻:')
print('在' + str(len(words['data'])) + '个' + js_link['data'][bianhao - 1][1] + '词汇当中，你认识其中' + str(
    len(danci)) + '个，实际掌握' + str(right_num) + '个，错误' + str(len(wrong_words)) + '个。')

save = input('是否打印并保存你的错词集？填入Y或N： ')
if save == 'Y':
    f = open('错题集.txt', 'a+')
    print('你记错的单词有：')
    f.write('你记错的单词有：\n')
    m = 0
    for z in wrong_words:
        m = m + 1
        print(z['content'])
        f.write(str(m + 1) + '. ' + z['content'] + '\n')
    print('你不认识的单词有：')
    f.write('你没记住的单词有：\n')
    s = 0
    for x in not_knows:
        print(x['content'])
        f.write(str(s + 1) + '. ' + x['content'] + '\n')
    print('错词和没记住的词已保存至当前文件目录下，下次见！')
else:
    print('下次见！')
