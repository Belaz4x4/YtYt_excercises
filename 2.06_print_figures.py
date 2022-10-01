"""
Модуль рисует выбранные пользователем фигуры по введенным параметрам.

Команды:
> ель - нарисовать ель
> ромб - нарисовать ромб
> выход - завершить программу
"""


def main():
    while True:
        command = input_command('Введите команду "> ель" "> ромб" или "> выход": ')
        if command == '> ель':
            print_fir()
        elif command == '> ромб':
            print_romb()
        elif command == '> выход':
            quit()
        else:
            print('Допустимые имена команд: ель, ромб, выход')


def input_command(message):
    while True:
        command = input(message).strip().lower()
        while '  ' in command:
            command = command.replace('  ', ' ')

        if not command.startswith('> '):
            print('Команда должна начинаться с ">"')
            continue
        if not command.strip('> ').isalpha():
            print('Имя команды должно состоять только из букв')
            continue

        return command


def print_fir():
    fir_height = input_height()
    fir_trunk = confirm('Нужен ли ствол: ')
    fir_symbol = input_symbol('Символ, которым нужно отрисовать ель: ')
    place_holder = input_symbol('Символ, которым нужно заполнить пустые места: ')

    picture_width = fir_height*2 + 1
    trunk_height = int(1 + fir_height * 0.2)

    for i in range(fir_height):
        print((fir_symbol*(1 + 2*i)).center(picture_width, place_holder))
    if fir_trunk:
        for _ in range(trunk_height):
            print(fir_symbol.center(picture_width, place_holder))


def print_romb():
    romb_height = input_height()
    romb_symbol = input_symbol('Символ, которым нужно отрисовать ромб: ')
    place_holder = input_symbol('Символ, которым нужно заполнить пустые места: ')

    if romb_height % 2 == 1:
        picture_width = romb_height + 2
    else:
        picture_width = romb_height + 1
    romb_center = romb_height/2

    for i in range(romb_height):
        if i < romb_center:
            print((romb_symbol * (1 + 2*i)).center(picture_width, place_holder))
        else:
            print((romb_symbol * (romb_height*2 - 2*i - 1)).center(picture_width, place_holder))


def input_height():
    while True:
        height = input('Введите высоту: ')

        if height.startswith('-'):
            print('Параметр должен быть положительным числом')
            continue
        if not height.isnumeric():
            print('Параметр должен быть целым числом')
            continue

        return int(height)


def confirm(message):
    while True:
        answer = input(message).lower().strip()

        if answer == 'да':
            return True
        elif answer == 'нет':
            return False
        else:
            print('Параметр должен иметь значение "да" или "нет" (в любом регистре)')


def input_symbol(message):
    while True:
        symbol = input(message)

        if len(symbol) == 1:
            return symbol

        print('Параметр должен состоять ровно из 1 символа')


main()