"""
Модуль принимает от пользователя его параметры и рассчитывает необходимое ему количество калорий.
"""


def calc_calories(weight, height, age, sex, activity_level):
    base_calories = calc_basic_calories(weight, height, age, sex)
    activity_coef = calc_activity_coef(activity_level)

    return round(base_calories * activity_coef)


def calc_basic_calories(weight, height, age, sex_coef):
    weight_limit = 30
    height_limit = 100
    age_limit = 14

    check_limit(weight, weight_limit, 'веса')
    check_limit(height, height_limit, 'роста')
    check_limit(age, age_limit, 'возраста')
    if sex == 'М':
        sex_coef = 5
    elif sex == 'Ж':
        sex_coef = -161
    else:
        raise ValueError('Неверное значение пола! Введите букву "М" или "Ж".')

    return 10 * weight + 6.25 * height - 5 * age + sex_coef


def calc_activity_coef(activity_level):
    if not (0 <= activity_level <= 4):
        raise ValueError('Неверное значение коэффициента активности! Введите цифру от 0 до 4')

    return 1.2 + activity_level * 0.175


def check_limit(value, limit, parameter):
    if value < limit:
        raise ValueError(f'Неверное значение {parameter}! Введите целое число не меньше {limit}.')


while True:
    try:
        weight = int(input('Введите ваш вес: '))
        height = int(input('Введите ваш рост: '))
        age = int(input('Введите ваш возраст: '))
        sex = input('Введите ваш пол (М/Ж): ').upper()
        activity_level = int(input('Рассчет коэффициента активности: \n'
                                   'Нет физических нагрузок и сидячая работа: 0\n'
                                   'Небольшие пробежки или легкая гимнастика 1–3 раза в неделю: 1\n'
                                   'Занятия спортом со средними нагрузками 3–5 раз в неделю: 2\n'
                                   'Полноценные тренировки 6–7 раз в неделю: 3\n'
                                   'Работа связана с физическим трудом + тренировки 2 раза в день, '
                                   'включая силовые упражнения: 4\n'
                                   'Введите коэффициент вашей активности: '))
        break
    except ValueError:
        print('Введено неверное значение! Попробуйте еще раз.')
        print('-' * 20)

try:
    value_of_calories = calc_calories(weight, height, age, sex, activity_level)
except ValueError as e:
    print('-' * 20)
    print(e)
else:
    print('-' * 20)
    print(f'Ваша дневная норма {value_of_calories} калорий.')