# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

from random import sample

def make_list(length):
    if length <= 0:
        return []
    nums_list = sample(range(length*2), length)
    return nums_list


# list = [2, 3, 4, 5, 6]
# list = [2, 3, 5, 6]
size = int(input("Введите длину списка: "))
my_list = make_list(size)

result = []
half_len = (len(my_list) // 2)
max_index = len(my_list) - 1

for i in range(half_len):
    multiply = my_list[i] * my_list[max_index - i]
    result.append(multiply)
#print(result)
if len(my_list) % 2 != 0:
    result.append(my_list[half_len] ** 2)
#print(result)

print(my_list)
print(result)