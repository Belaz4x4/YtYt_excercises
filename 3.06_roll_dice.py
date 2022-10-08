"""
Модуль совершает заданное количество бросков игральной кости с заданным количеством граней.
На экран выводится количество выпадений каждой грани и его доля от общего количества бросков.
"""

from random import randint


def roll_dice(n, sides_number=6):
    check_number(n, 1)
    check_number(sides_number, 4)

    results_list = [0 for _ in range(sides_number)]

    for _ in range(n):
        side = randint(1, sides_number)
        results_list[side - 1] += 1

    return results_list


def print_results(results_list):
    n = sum(results_list)

    print(f'Всего бросков: {n}')
    for i, drops in enumerate(results_list, 1):
        drop_percent = drops * 100 / n
        print(f'{i}: {drops} ({drop_percent:.2f}%)')


def check_number(number, limit):
    if number < limit:
        raise ValueError(f'Количество граней должно быть не менее {limit}!')


results = roll_dice(100000, 8)
print_results(results)

