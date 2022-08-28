print('Задача 1. Урок информатики 2')


# В прошлый раз учитель написал программу,
# которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля.
# 
# Задано положительное число x (x > 0).
# Ваша задача преобразовать его в формат плавающей точки,
# то есть x = a * 10 ** b, где 1 ≤ а < 10
# 
# Обратите внимание, что x теперь больше нуля, а не больше единицы.
# Обеспечьте контроль ввода.
# 
# Пример 1:
# 
# Введитечисло: 92345
# 
# Формат плавающей точки: x = 9.2345 * 10 ** 4
# 
# Пример 2:
# 
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3
print('Задача 3. Приоритет задач')
def numeral_count(number):
    count = 0
    while number:
        number //= 10
        count += 1
    return count

def numeral_check(n):
    max_count = 0
    max_number = 0
    for _ in range(1, n + 1):

        new_value = int(input("Введите число: "))
        if new_value < 0:
            new_value = 0

        cipher_count = numeral_count(new_value)
        if cipher_count > max_count:
            max_count = cipher_count
            max_number = new_value

    return max_number


