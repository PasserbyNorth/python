# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 3

# 1 2 3 4 5
# Вывод: 1

import random

arrLen = int(input('Введите длинну массива: '))
target = int(input('Введите искомую цифру: '))

randomArr = [random.randint(1, arrLen//2) for i in range(arrLen)]

print(randomArr)

print(f'цифрa {target} встречается в массиве {randomArr.count(target)} раз')
