# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 2 -> 10
# 3 -> 11

from os import sep

num = int(input('Введите число: '))
list_result = []
count = 0
while num:
    result = num % 2
    list_result.append(result)
#    print(result)
    num = num // 2
#    print(num)
    count=+1
#print(list_result)
print(*list_result[::-1], sep = "")

