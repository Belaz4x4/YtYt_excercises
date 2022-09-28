"""
Модуль в процессе написания.
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
            print('Неправильная команда!')


def input_command(message):
    command = input(message).strip().lower()
    while '  ' in command:
        command = command.replace('  ', ' ')
    return command


def print_fir():
    height = input('Введите высоту без учёта ствола (целое положительное число): ')
    fir_trunk = input('Нужен ли ствол ("да" или "нет")').lower()
    fir_symbol = input('Введите символ, которым должна быть отрисована ель: ')
    place_holder = input('Введите символ-заполнитель:')


def print_romb():
    pass



main()