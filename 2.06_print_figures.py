"""
Модуль рисует выбранные пользователем фигуры по введенным параметрам.

Команды:
> ель - нарисовать ель
> ромб - нарисовать ромб
> выход - завершить программу
"""


def main():
    while True:
        command = input_command('Введите команду: ')

        if command == '> ель':
            fir_height = input_int('Введите высоту: ')
            fir_trunk = input_confirmation('Нужен ли ствол: ')
            fir_symbol = input_symbol('Символ, которым нужно отрисовать ель: ')
            place_holder = input_symbol('Символ, которым нужно заполнить пустые места: ')

            print_fir(fir_height, fir_trunk, fir_symbol, place_holder)
        elif command == '> ромб':
            rhomb_height = input_int('Введите высоту: ')
            rhomb_symbol = input_symbol('Символ, которым нужно отрисовать ромб: ')
            place_holder = input_symbol('Символ, которым нужно заполнить пустые места: ')

            print_rhomb(rhomb_height, rhomb_symbol, place_holder)
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


def print_fir(fir_height, fir_trunk, fir_symbol, place_holder):
    picture_width = fir_height*2 + 1
    trunk_height = int(1 + fir_height*0.2)

    for i in range(fir_height):
        print((fir_symbol*(1 + 2*i)).center(picture_width, place_holder))
    if fir_trunk:
        for _ in range(trunk_height):
            print(fir_symbol.center(picture_width, place_holder))


def print_rhomb(rhomb_height, rhomb_symbol, place_holder):
    picture_width = rhomb_height + 1
    if rhomb_height % 2 == 1:
        picture_width += 1

    rhomb_center = rhomb_height / 2

    for i in range(rhomb_height):
        if i < rhomb_center:
            print((rhomb_symbol * (1 + 2*i)).center(picture_width, place_holder))
        else:
            print((rhomb_symbol * (rhomb_height*2 - 2*i - 1)).center(picture_width, place_holder))


def input_int(message):
    while True:
        parameter = input(message)

        if parameter.startswith('-'):
            print('Параметр должен быть положительным числом')
            continue
        if not parameter.isnumeric():
            print('Параметр должен быть целым числом')
            continue

        return int(parameter)


def input_confirmation(message):
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