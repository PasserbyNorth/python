# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import math


file = open('hw/hw2/task12/input.txt')

inputValue = list(file)[0].split()

S = int(inputValue[0])
P = int(inputValue[1])

x = (S - math.sqrt(S**2-4*P))/2
y = S - x

outputVale = open('hw/hw2/task12/output.txt', 'w')
outputVale.write(f'x = {int(x)} y = {int(y)}')

outputVale.close()

