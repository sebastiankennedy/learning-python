import os

list_test = ['一弦一柱思华年。\n','只是当时已惘然。\n']

with open ('poem3.txt','r') as f:
    lines = f.readlines()

with open('poem_new.txt','w') as new:
    for line in lines:
        if line in list_test:
            new.write('____________。\n')
        else:
            new.write(line)

os.replace('poem_new.txt', 'poem3.txt')
