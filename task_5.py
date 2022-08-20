print('Задача 5. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр
# и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами,
# вам нужно было написать код по следующим условиям:
# программа получает на вход два числа.
#
# В первом числе должно быть не меньше трёх цифр,
# во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами,
# а затем выводится их сумма.
#
#
# И тут вы натыкаетесь на программу,
# которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код,
# чтобы он не выглядел так ужасно.
# Да и вам самим становится, мягко говоря, не по себе от него.
#
# Разбейте приведённую ниже программу на функции.
# Повторений кода должно быть как можно меньше.
# Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.
def number_count(first_number, second_number):
    first_number_count = len(str(first_number))
    second_number_count = len(str(second_number))
    if (first_number_count != 3):
        print(f'Ошибка! В числе {first_number} не достаточно символов')
        return exit()
    elif (second_number_count != 4):
        print(f'Ошибка! В числе {second_number} не достаточно символов')
        return exit()
    else:
        first_number = coup(first_number, first_number_count)
        second_number = coup(second_number, second_number_count)
        return first_number, second_number

def coup(temporary_number, long_number):
    last_digit = temporary_number % 10
    first_digit = temporary_number // 10 ** (long_number- 1)
    between_digits = temporary_number % 10 ** (long_number - 1) // 10
    number = last_digit * 10 ** (long_number - 1) + between_digits * 10 + first_digit
    return number

print('Введите два числа: первое должно быть не меньше трех символов, второе - четырех\n')
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

first_number, second_number = number_count(first_number, second_number)

print(f'\nИзменённое первое число: {first_number}')
print(f'Изменённое второе число: {second_number}')
print(f'\nСумма чисел: {first_number + second_number}')

exit()
