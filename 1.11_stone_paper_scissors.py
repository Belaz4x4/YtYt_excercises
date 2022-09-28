"""
Программа играет с пользователем в Камень-ножницы-бумага до трех побед.
"""

from random import randint

STONE = 'Камень'
SCISSORS = 'Ножницы'
PAPER = 'Бумага'

figures = [STONE, SCISSORS, PAPER]

programs_score = 0
users_score = 0

while programs_score != 3 and users_score != 3:
    users_figure = input('Что вы загадаете?\n')

    while users_figure not in figures:
        users_figure = input(f'Выберите фигуру: "{figures[0]}", "{figures[1]}" или "{figures[2]}"\n')

    number_of_figure = randint(1, 3) - 1
    programs_figure = figures[number_of_figure]

    print(f'Программа загадала {programs_figure}\n')

    if users_figure == programs_figure:
        print('Ничья!')

    elif ((users_figure == STONE and programs_figure == SCISSORS)
            or (users_figure == SCISSORS and programs_figure == PAPER)
            or (users_figure == PAPER and programs_figure == STONE)):
        users_score += 1
        print('Вы победили!')

    else:
        programs_score += 1
        print('Победила программа!')

    print(f'Счет {users_score} : {programs_score}')
    print('----------')

if users_score == 3:
    print(f'Вы победили со счетом {users_score} : {programs_score} !')
else:
    print(f'Вы проиграли со счетом {users_score} : {programs_score} !')
