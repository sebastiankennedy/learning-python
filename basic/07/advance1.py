import time
import random

player_victory = 0
enemy_victory = 0

while True:
    for i in range(1, 4):
        time.sleep(1.5)
        print('\n{}{}{}'.format('——————现在是第 ', i, ' 局——————'))
        player_life = random.randint(100, 150)
        player_attack = random.randint(30, 50)
        enemy_life = random.randint(100, 150)
        enemy_attack = random.randint(30, 50)

        print('{}{}{}{} '.format('【玩家】\n血量：', player_life, '\n攻击：', player_attack))
        print('------------------------')
        time.sleep(1)
        print('{}{}{}{}'.format('【敌人】\n血量：', enemy_life, '\n攻击：', enemy_attack))
        print('-----------------------')
        time.sleep(1)

        while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack
            enemy_life = enemy_life - player_attack
            print('{}{}'.format('敌人发起了攻击，【玩家】剩余血量', player_life))
            print('{}{}'.format('你发起了攻击，【敌人】的血量剩余', enemy_life))
            print('-----------------------')
            time.sleep(1.2)

        if player_life > 0 and enemy_life <= 0:
            player_victory += 1
            print('敌人死翘翘了，你赢了！')
        elif player_life <= 0 and enemy_life > 0:
            enemy_victory += 1
            print('悲催，敌人把你干掉了！')
        else:
            print('哎呀，你和敌人同归于尽了！')

    if player_victory > enemy_victory:
        time.sleep(1)
        print('{}{}'.format('\n', '【最终结果：你赢了！】'))
    elif enemy_victory > player_victory:
        print('{}{}'.format('\n', '【最终结果：你输了！】'))
    else:
        print('{}{}'.format('\n', '【最终结果：平局！】'))

    a1 = input('要继续游戏吗，请输入n退出，输入其他继续：')
    if a1 == 'n':
        break
