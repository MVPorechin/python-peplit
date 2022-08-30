print('Задача 2. Функция максимума')

# Юра пишет различные полезные функции для Питона, 
# чтобы остальным программистам стало проще работать.

# Он захотел написать функцию, 
# которая будет находить максимум из перечисленных чисел.
# Функция для нахождения максимума из двух чисел у него уже есть.
 
# Юра задумался: может быть, её можно как-то использовать 
# для нахождения максимума уже от трёх чисел?
 
 
# Напишите программу, 
# которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.
def maximum_number(number_one, number_two):
  return (number_one + number_two + abs(number_one - number_two)) / 2

number_one = float(input('Введите первое число: '))
# number_two = float(input('Введите второе число: '))
# number_three = float(input('Введите третье число: '))
number_two = float(input('Введите второе число: '))
number_three = float(input('Введите третье число: '))


maximum_between_number = maximum_number(number_one, number_two)
print(f'Максимум из трех чисел: {maximum_number(maximum_between_number, number_three)}')