# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший.

# Ввод: 5
# Ввод: 6
# 1 2 0 4 7
# Вывод: 7

import random

arrLen = int(input('Введите длинну массива: '))
target = int(input('Введите искомую цифру: '))

randomArr = [random.randint(1, arrLen//2) for i in range(arrLen)]
print(randomArr)

f_target = [abs(randomArr[i]-target) for i in range(len(randomArr))]

print(f'Ближайшее по значению число к искомому: {randomArr[f_target.index(min(f_target))]}')