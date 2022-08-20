print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225

def number_backwards(number):
  number_backwards = ''
  for symbol in number:
    number_backwards = symbol + number_backwards
  return number_backwards

def summ():
    summ = int(number_backwards(first_number)) + int(number_backwards(second_number))
    return summ

first_number = input('Введите первое число: ')
second_number = input('Введите второе число: ')

print(f'\nПервое число наоборот: {number_backwards(first_number)}')
print(f'Второе число наоборот: {number_backwards(second_number)}')
print(f'\nСумма: {summ()}')
print(f'Сумма наоборот: {number_backwards(str(summ()))}')