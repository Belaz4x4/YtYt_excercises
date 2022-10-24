"""
Модуль ведет складской учет.
Основная функция: inventory_accounting()
"""


def show_stock_balance():
    print('Остаток на складе:')
    for good, amount in main_stock_balance.items():
        print(f'{good}: {amount}')


def add_goods(good, amount):
    amount = int(amount)
    if good in main_stock_balance:
        main_stock_balance[good] += amount
    else:
        main_stock_balance[good] = amount
    print(f'Добавлено: {amount} {good}')


def pick_goods(good, amount):
    amount = int(amount)
    if good not in main_stock_balance:
        print(f'Ошибка: Товар {good} не найден')
    elif main_stock_balance[good] >= amount:
        main_stock_balance[good] -= amount
        print(f'Получено со склада: {amount} {good}')
    else:
        print('Ошибка: Недостаточно товара на складе')


def inventory_accounting():
    """
    Функция ведет складской учет.
    Доступные команды:
    info - показать остатки на складе.
    add#наименование товара#количество товара цифрами - добавить товар на склад
    pick#наименование товара#количество товара цифрами - получить товар со склада
    '' - выход
    """
    while True:
        command = input()
        command_values = command.split(sep='#')
        command_name = command_values[0]
        if command_name not in commands:
            print('Ошибка: введена неверная команда.')
            print('Доступные команды:', *commands)
        elif len(command_values) == 1:
            commands[command_name]()
        else:
            try:
                commands[command_name](*command_values[1:])
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
        '': quit,
        'info': show_stock_balance,
        'add': add_goods,
        'pick': pick_goods
    }

    print(inventory_accounting.__doc__)
    inventory_accounting()
