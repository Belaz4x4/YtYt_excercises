"""
Модуль конвертирует  число от 1 до 999 миллиардов в строку.
Основная функция: to_numeral(number)
"""
numbers_as_strings = {
    0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
    6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять',
    11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 20: 'двадцать', 30: 'тридцать',
    40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят',
    90: 'девяносто', 100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста',
    500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот', 800: 'восемьсот', 900: 'девятьсот',
}


def to_numeral(number):
    """
    Функция разбивает число на элемнты по три цифры, которые соответствуют сотням, тысячам, миллионам и миллиардам.
    После чего, для каждого элемента формирует свою часть описания и возвращает суммарный результат.
    """
    number = str(number)
    hundreds = number[-3:]
    thousands = number[-6:-3]
    millions = number[-9:-6]
    billions = number[:-9]
    message = ''

    if billions:
        message += (convert_triplets(billions) + ' миллиард' + _ending_of_millions_and_billions(billions))
    if millions:
        message += (convert_triplets(millions) + ' миллион' + _ending_of_millions_and_billions(millions))
    if thousands:
        thousands_message = convert_triplets(thousands)
        thousands_message = thousands_message.replace('один', 'одна')
        thousands_message = thousands_message.replace('два', 'две')
        message += (thousands_message + ' тысяч' + _ending_of_thousands(thousands))
    if hundreds:
        message += convert_triplets(hundreds)

    return message.capitalize().rstrip()


def convert_deuces(number):
    if number <= 13:
        return numbers_as_strings[number]
    elif 13 < number < 20:
        units = number % 10
        return numbers_as_strings[units][:-1] + 'надцать'
    elif 20 <= number <= 99:
        units = number % 10
        tens = number - units
        return numbers_as_strings[tens] + ' ' + numbers_as_strings[units]


def convert_triplets(number):
    number = int(number)
    if 1 <= number <= 99:
        message = convert_deuces(number % 100)
    elif 100 <= number <= 999:
        hundreds = number // 100 * 100
        message = numbers_as_strings[hundreds] + ' ' + convert_deuces(number % 100)
    elif number == 0:
        message = ''
    return message


def _ending_of_millions_and_billions(number):
    end_of_number = int(number[-1])
    if end_of_number == 0 or 5 <= end_of_number <= 9:
        return 'ов '
    elif end_of_number == 1:
        return ' '
    elif 2 <= end_of_number <=4 :
        return 'а '


def _ending_of_millions_and_billions(number):
    end_of_number = int(number[-1])
    if end_of_number == 0 or 5 <= end_of_number <= 9:
        return 'ов '
    elif end_of_number == 1:
        return ' '
    elif 2 <= end_of_number <=4 :
        return 'а '


def _ending_of_thousands(number):
    end_of_number = int(number[-1])
    if end_of_number == 0 or 5 <= end_of_number <= 9:
        return ' '
    elif end_of_number == 1:
        return 'а '
    elif 2 <= end_of_number <=4 :
        return 'и '


# Тесты:
assert to_numeral(123456789) == (
    'Сто двадцать три миллиона '
    'четыреста пятьдесят шесть тысяч '
    'семьсот восемьдесят девять'
)
assert to_numeral(1000) == 'Одна тысяча'
assert to_numeral(102010) == 'Сто две тысячи десять'
assert to_numeral(2019) == 'Две тысячи девятнадцать'
assert to_numeral(202019) == 'Двести две тысячи девятнадцать'


