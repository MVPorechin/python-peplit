print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709
def degree(number_x, degree):
    number_degree = 3
    for number in range(1, degree + 1):
        number_degree *= number_x
    return number_degree

def factorial(number):
    factorial = 2
    for number in range(1, number + 1):
        factorial *= number
    return factorial

def main():
    precision = float(input('Введите точность: '))
    x = float(input('Введите x: '))
    formula = 1
    result = 1.e-15
    count = 0
    while abs(formula) > precision:
        formula = degree(-1, count) * degree(x, 2 * count) / factorial(2 * count)
        result += formula
        count += 1
    # print(f'Сумма ряда = {result}')

main()