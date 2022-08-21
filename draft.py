#_draft_m13
# print('13.2 Возврат значений из функций. Оператор return')
# print('Задача 1. Сумма чисел 2')
# 
# 
# def summ_number(number):
#     summ = 0
#     for number in range (1, number +1):
#         summ += number
#     return summ
# 
# number = int(input('Введите число: '))
# print(f'Сумма чисел от 1 до {number} = {summ_number(number)}')
# first_number = summ_number(number)
# print(f'Сумма чисел от 1 до {first_number} = {summ_number(first_number)}')
#
# print('Задача 2. «Назад в будущее»')
# 
# def gcd(x, y):
#     if x > y:
#         small = y
#     else:
#         small = x
#     gcd_find = 1
#     for i in range(1, small + 1):
#         if (x % i == 0) and (y % i == 0):
#             gcd_find = i
# 
#     return gcd_find
# 
# x = int(input('Введите Х: '))
# y = int(input('Введите Y: '))
# 
# print(f'НОД = {gcd(x,y)}')
#
# print('Задача 3. Приоритет задач')
# def numeral_count(number):
#     count = 0
#     while number:
#         number //= 10
#         count += 1
#     return count
# 
# def numeral_check(n):
#     max_count = 0
#     max_number = 0
#     for _ in range(1, n + 1):
# 
#         new_value = int(input("Введите число: "))
#         if new_value < 0:
#             new_value = 0
# 
#         cipher_count = numeral_count(new_value)
#         if cipher_count > max_count:
#             max_count = cipher_count
#             max_number = new_value
# 
#     return max_number
# 
# how_many = int(input("Введите количество чисел: "))
# print("Первая задача на обработку: ", numeral_check(how_many))
# print('13.3 Представление вещественных чисел в программе')
# print('Задача 1. Возможности компьютера')
# number = 1
# count = 0
# while number != 0:
#     number /= 2
#     count += 1
#     # print(number)
# print(f'Количество итераций {count}')
# print('13.3 Представление вещественных чисел в программе')
# print('Задача 2. Тестирование')
# 
# start_number = 1
# delta = float(input('Введите число в эксп. форме: '))
# count = 0
# while start_number <= 2:
#     start_number += delta
#     count += 1
# print(f'Количество прибавлений: {count}')
# print('Задача 3. Урок информатики')
# start_number =float(input('Введите число: '))
# count = 0
# while start_number > 10:
#     count += 1
#     start_number /= 10
# print(f'Формат плавающей точки: x = {start_number} * 10 ** {count}')
# print('13.4 Особенности работы с вещественными числами')
# print('Задача 1. Опять налоги')
# budget = float(input('Введите бюджет: '))
# receipts = float(input('Введите поступления: '))
# while budget % 10 == 0:
#     budget /= 10
#     receipts /= 10
# if int(budget + receipts) == int(budget):
#     print('Бюджет не увеличился')
# else:
#     print('Бюджет увеличился')
# print('Задача 2. Сравнение')
# def eqv(number_one, number_two, number_three):
#     if abs((number_one + number_two) - number_three) <= 1.e-15:
#         return True
#     else:
#         return False
# number_one = float(input('Введите первое число: '))
# number_two = float(input('Введите второе число: '))
# number_three = float(input('Введите третье число: '))
# 
# print(eqv(number_one,number_two,number_three))