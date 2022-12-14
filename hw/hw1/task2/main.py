# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
print('')

temp = 0

while not temp:
    target = input('Введите число: ')
    if not target.isnumeric():
        print('Вы ввели не число!')
    else:
        for i in target:
            temp += int(i)
    print(f'Результат = {temp}\n') if temp > 0 else print('')
