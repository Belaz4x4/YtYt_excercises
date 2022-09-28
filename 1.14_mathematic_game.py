"""
Эта программа генерирует случайные математические примеры на сложение, вычетание и умножение
и проверяет ответы пользователя в бесконечном цикле.

stop, '' - выход из программы
"""

from random import randint

print('Эта программа генерирует случайные математические примеры '
      'на сложение, вычетание и умножение '
      'и проверяет ваши ответы.')

while True:
    max_number = input('Введите максимально возможное число в примере: ')
    if max_number.isnumeric():
        max_number = int(max_number)
        break
    else:
        print('Неверное значение! Введите целое положительное число')

print()

while True:
    a = randint(-max_number, max_number)
    b = randint(-max_number, max_number)
    answers = [a + b, a - b, a * b]
    operators = ['+', '-', '*']
    generator = randint(0, 2)
    answer = answers[generator]
    operator = operators[generator]
    math_question = f'{a} {operator} {b} ='

    while True:
        users_answer = input(f'{math_question} ?\n')
        if users_answer == 'stop' or users_answer == '':
            quit()

        try:
            users_answer = int(users_answer)
            break
        except ValueError:
            print('Неверное значение! Введите число цифрами '
                  'или остановите программу введя пустое значение или "stop"')

    if users_answer == answer:
        print('Верно!')
    else:
        print(f'Неверно! {math_question} {answer}')

    print()
