print('Задача 9. Аннуитетный платёж')

# Кредит в сумме S млн руб.,
# выданный на n лет под i% годовых,
# подлежит погашению равными ежегодными выплатами в конце каждого года,
# включающими процентные платежи и сумму в погашение основного долга.
#
# Проценты начисляются в один раз в год.
# После выплаты третьего платежа
# достигнута договорённость между кредитором и заёмщиком
# о продлении срока погашения займа на n_2 лет
# и увеличении процентной ставки с момента конверсии до i_2%.
#
# Напишите программу,
# которая выводит план погашения оставшейся части долга.
#
# A = KS
#
# K = i(1 + i) ** n / (1 + i) ** n - 1
#
# Пример:
#
# Введите сумму кредита: 40e6
# На сколько лет выдан? 5
# Сколько процентов годовых? 6
#
# Период: 1
#
# Остаток долга на начало периода: 40000000.0
# Выплачено процентов: 2400000.0
# Выплачено тела кредита: 7095856.02
#
#
# Период: 2
#
# Остаток долга на начало периода: 32904143.98
# Выплачено процентов: 1974248.6387999998
# Выплачено тела кредита: 7521607.3812
#
# Период: 3
#
# Остаток долга на начало периода: 25382536.5988
# Выплачено процентов: 1522952.195928
# Выплачено тела кредита: 7972903.824072
#
# Остаток долга: 17409632.774728
#
# =================================================
#
# На сколько лет продляется договор? 2
# Увеличение ставки до: 10
#
# Период: 1
#
# Остаток долга на начало периода: 17409632.774728
# Выплачено процентов: 1740963.2774728
# Выплачено тела кредита: 3751267.5625271997
#
# Период: 2
#
# Остаток долга на начало периода: 13658365.2122008
# Выплачено процентов: 1365836.52122008
# Выплачено тела кредита: 4126394.3187799198
#
# Период: 3
#
# Остаток долга на начало периода: 9531970.89342088
# Выплачено процентов: 953197.0893420881
# Выплачено тела кредита: 4539033.750657911
#
# Период: 4
#
# Остаток долга на начало периода: 4992937.142762969
# Выплачено процентов: 499293.71427629696
# Выплачено тела кредита: 4992937.125723703
#
# Остаток долга: 0.017039266414940357
def payment(credit_amount, loan_duration, percent_credit):
  annuity_payment = round((percent_credit * ((1 + percent_credit) ** loan_duration)) / (((1 + percent_credit) ** loan_duration) - 1) * credit_amount, 2)
  return annuity_payment

# def payment(credit_amount, loan_duration, percent_credit):
#   annuity_payment = round((percent_credit * ((1 + percent_credit) ** loan_duration)) / (((1 + percent_credit) ** loan_duration) - 1) * credit_amount, 2)
#   return annuity_payment

def period(loan_amount, period, annuity_pay, percent_credit):
  count = 0
  for years in range(period, 0, -1):
    interest_paid = loan_amount * percent_credit
    body_paid = annuity_pay - interest_paid
    print(f'\nПериод: {count}')
    print(f'Остаток долга на начало периода: {loan_amount}')
    print(f'Выплачено процентов: {interest_paid}')
    print(f'Выплачено тела кредита: {body_paid}')
    loan_amount -= body_paid
    count += 1
    if years == 1:
      print(f'\nОстаток долга: {loan_amount} \n')
      print('*' * 20)
      break
  return loan_amount

credit_amount = float(input('\nВведите сумму кредита: '))
loan_duration = int(input('На сколько лет выдан?: '))
first_percent = float(input('Сколько процентов годовых?: '))
first_percent /= 100

annuity_payment = payment(credit_amount, loan_duration, first_percent)
years_passed = 3
body_credit = period(credit_amount, years_passed, annuity_payment, first_percent)

contract_extension = int(input('На сколько лет продлевается договор?: '))
contract_extension += loan_duration - years_passed
second_percent = float(input('Увеличение ставки до: '))
second_percent /= 100

annuity_payment = payment(body_credit, contract_extension, second_percent)
body_credit = period(body_credit, contract_extension, annuity_payment, second_percent)
