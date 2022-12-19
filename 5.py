"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
 При нажатии Enter должна выводиться сумма чисел.
 Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать
 Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после
нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
 сумме и после этого завершить программу.
"""


def sum():
    sum_res = 0
    ext = False
    while ext == False:
        numb = input('Введите числа через пробел. Для завершения программы введите "q" ').split()
        res = 0
        for el in range(len(numb)):
            if numb[el] == 'q':
                ext = True
                break
            else:
                res = res + int(numb[el])
        sum_res = sum_res + res
        print(f'Сумма = {sum_res}')
    print(f'Общая сумма = {sum_res}')


sum()