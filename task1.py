# Задание 4/ Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

# n = int(input('введите целое положительное число N= '))

# lst = [int(input()) for _ in range(n)]
# print(lst)



n = int(input('введите целое положительное число N= '))
a = int(input(f'введите позицию первого элемента - от 0 до {n*2}: '))
b = int(input(f'введите позицию второго элемента - от 0 до {n*2}: '))
lst = [i for i in range(-n,n+1)]
print(f'{lst}\n произведение элементов равно: {lst[a]*lst[b]}')
