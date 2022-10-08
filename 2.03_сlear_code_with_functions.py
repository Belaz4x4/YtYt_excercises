"""
Программа запрашашивает у пользователя ширину и высоту экрана в пикселях
и выводит на зкрон разрешение и общее количество пикселей.
"""


def input_of_value(message: str):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print('Неверное значение! Введите целое число.')


def print_screen_resolution(width, height):
    print(f'Разрешение экрана {width}x{height} пикселей.')
    print(f'Всего {width * height} пикселей.')


screen_width = input_of_value('Введите количество пикселей по горизонтали: ')
screen_height = input_of_value('Введите количество пикселей по вертикали: ')

print_screen_resolution(screen_width, screen_height)