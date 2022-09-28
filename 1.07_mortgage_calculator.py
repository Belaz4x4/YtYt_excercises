"""
Модуль расчитывает аннуитетный платеж по ипотеке на основании введенных данных.
"""

cost_of_apartment = float(input('Введите стоимость квартиры/дома: '))
initial_payment = float(input('Введите первоначальный взнос: '))
loan_term = float(input('Введите срок займа в годах: '))
interest_rate = float(input('Введите процентную ставку по ипотеке: '))
insurance = float(input('Введите стоимость страховки в процентах от стоимости квартиры/дома: '))

monthly_rate = interest_rate / 1200
general_rate = (1 + monthly_rate) ** (loan_term * 12)
loan_amount = cost_of_apartment - initial_payment
monthly_payment = loan_amount * monthly_rate * general_rate / (general_rate - 1)
annual_insurance = cost_of_apartment * insurance / 100
annual_insurance_per_month = annual_insurance / 12
total_monthly_payment = monthly_payment + annual_insurance_per_month

print('-' * 20)
print(f'Сумма кредита: {int(loan_amount)} рублей.')
print(f'Ежемесячный платеж по ипотеке: {int(monthly_payment)} рублей.')
print(f'Стоимость ежегодной страховки: {int(annual_insurance)} рублей.')
print(f'Стоимость ежегодной страховки, "размазанной" помесячно: {int(annual_insurance_per_month)} рублей.')
print(f'Итоговый ежемесячный платеж: {int(total_monthly_payment)} рублей.')