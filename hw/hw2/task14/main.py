# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

Number = int(input('Введите число: '))

square = 1

while square <= Number:
    print(f'{square}')
    square *= 2