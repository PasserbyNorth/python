# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2


with open('hw/hw2/task10/coins.txt', 'r') as file:
    coinValue = file.read()
    # print(coinValue)
    heads = 0
    tails = 0
    for i in coinValue:
        if int(i) == 1:
            heads += 1
        else:
            tails += 1

print(f'нужно перевернуть {heads} орлов' if heads < tails else f'нужно перевернуть {tails} решек')