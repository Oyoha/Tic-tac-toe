def play():
    newbattleground = [[' ', '1', '2', '3'], ['1', '-', '-', '-'], ['2', '-', '-', '-'], ['3', '-', '-', '-']]
    turn = 0
    while turn < 9 or checkwin(newbattleground):
        print('Ход', turn + 1)
        print('Ваше игровое поле')
        showbattleground(newbattleground)
        if turn % 2 == 0:
            print('Ход', players[0])
            i = int(input('Выбирите столбец, куда вы хотите поставить крестик: '))
            j = int(input('Выбирите строку, куда вы хотите поставить крестик: '))
            if j <= 3 and i <= 3 and newbattleground[j][i] == '-':
                newbattleground[j][i] = 'X'
            else:
                print('Данное поле уже занято или вы пытаетесь сходить вне поля! Попробуйте заново!')
                continue
        else:
            print('Ход', players[1])
            i = int(input('Выбирите столбец, куда вы хотите поставить нолик: '))
            j = int(input('Выбирите строку, куда вы хотите поставить нолик: '))
            if j <= 3 and i <= 3 and newbattleground[j][i] == '-':
                newbattleground[j][i] = '0'
            else:
                print('Данное поле уже занято или вы пытаетесь сходить вне поля! Попробуйте заново!')
                continue

        if checkwin(newbattleground) is False:
            showbattleground(newbattleground)
            print('Выйграл ', players[turn % 2], '!')
            break
        else:
            turn += 1
        if turn == 9:
            showbattleground(newbattleground)
            print('Ничья!')


def showbattleground(newbattleground):
    for i in newbattleground:
        print(*i)


def checkwin(newbattleground):
    if (newbattleground[1][1] == newbattleground[1][2] == newbattleground[1][3] and newbattleground[1][1] != '-' or
            newbattleground[2][1] ==
            newbattleground[2][2] == newbattleground[2][3] and newbattleground[2][1] != '-' or newbattleground[3][1] ==
            newbattleground[3][2] ==
            newbattleground[3][3] and newbattleground[3][1] != '-' or newbattleground[1][1] == newbattleground[2][1] ==
            newbattleground[3][1] and newbattleground[1][1] != '-' or
            newbattleground[1][2] == newbattleground[2][2] == newbattleground[3][2] and newbattleground[1][2] != '-' or
            newbattleground[1][3] ==
            newbattleground[2][3] == newbattleground[3][3] and newbattleground[1][3] != '-' or newbattleground[1][1] ==
            newbattleground[2][2] ==
            newbattleground[3][3] and newbattleground[1][1] != '-' or newbattleground[1][3] == newbattleground[2][2] ==
            newbattleground[3][1] and newbattleground[1][3] != '-'):
        return False


players = [input('Введите имя первого игрока: '), input('Введите имя второго игрока: ')]
flag = True
while flag:
    play()
    newgame = input('Хотите сыграть еще раз? Напишите Y, если да, напишите N, если нет: ')
    if newgame.lower() == 'y':
        players[0], players[1] = players[1], players[0]
    else:
        flag = False

print('Спасибо за игру! До встречи!!!')
