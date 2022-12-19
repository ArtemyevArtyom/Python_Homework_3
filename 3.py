"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""

def my_func(arg1, arg2, arg3):
    min_arg = min(arg1, arg2, arg3)
    sum_two_max = arg1 + arg2 + arg3 - min_arg
    return sum_two_max


result = my_func(int(input('Введите аргумент 1: ')),
                 int(input('Введите аргумент 2: ')),
                 int(input('Введите аргумент 3: ')))
print(result)