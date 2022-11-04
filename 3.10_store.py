"""
Модуль ведет складской учет.
Основная функция: inventory_accounting()
"""


def inventory_accounting(commands, stock_balance):
    """
    Функция ведет складской учет. Принимает словарь, содержащий принимаемые комманды и словарь содержащий
    складские остатки.

    """
    print('\tДоступные команды:')
    for func in commands.values():
        print(func.__doc__)
    print("\t'' - выход")

    while True:
        command = input()
        command_values = command.split(sep='#')
        command_name = command_values[0]
        if command_name == '':
            quit()
        elif command_name not in commands:
            print('Ошибка: введена неверная команда.')
            print('Доступные команды:', *commands)
        elif len(command_values) == 1:
            commands[command_name](stock_balance)
        else:
            try:
                commands[command_name](stock_balance, *command_values[1:])
            except (ValueError, TypeError):
                print('Ошибка: введены неверные данные для команды.')
        print()


def show_stock_balance(stock_balance):
    """
    info - показать остатки на складе.
    """
    print('Остаток на складе:')
    for good, amount in stock_balance.items():
        print(f'{good}: {amount}')


def add_goods(stock_balance, good, amount):
    """
    add#наименование товара#количество товара цифрами - добавить товар на склад
    """
    amount = int(amount)
    if good in stock_balance:
        stock_balance[good] += amount
    else:
        stock_balance[good] = amount
    print(f'Добавлено: {amount} {good}')


def pick_goods(stock_balance, good, amount):
    """
    pick#наименование товара#количество товара цифрами - получить товар со склада
    """
    amount = int(amount)
    if good not in stock_balance:
        print(f'Ошибка: Товар {good} не найден')
    elif stock_balance[good] >= amount:
        stock_balance[good] -= amount
        print(f'Получено со склада: {amount} {good}')
    else:
        print('Ошибка: Недостаточно товара на складе')


def inventory_accounting(commands, stock_balance):
    """
    Функция ведет складской учет. Принимает словарь, содержащий принимаемые комманды и словарь содержащий
    складские остатки.

    """
    print('\tДоступные команды:')
    for func in commands.values():
        print(func.__doc__)
    print("\t'' - выход")

    while True:
        command = input()
        command_values = command.split(sep='#')
        command_name = command_values[0]
        if command_name == '':
            quit()
        elif command_name not in commands:
            print('Ошибка: введена неверная команда.')
            print('Доступные команды:', *commands)
        elif len(command_values) == 1:
            commands[command_name](stock_balance)
        else:
            try:
                commands[command_name](stock_balance, *command_values[1:])
            except (ValueError, TypeError):
                print('Ошибка: введены неверные данные для команды.')
        print()


if __name__ == '__main__':
    main_stock_balance = {
        'Самокаты': 32,
        'Велосипеды': 19,
        'Гироскутеры': 47
    }

    commands = {
        'info': show_stock_balance,
        'add': add_goods,
        'pick': pick_goods
    }

    inventory_accounting(commands, main_stock_balance)
