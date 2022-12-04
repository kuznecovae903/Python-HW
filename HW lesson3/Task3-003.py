# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19`

from random import uniform

def make_list(length):
    if length <= 0:
        return []

    float_nums_list = []
    for elem in range(length):
        num = round(uniform(1, 10), 2)
        float_nums_list.append(num)

    return float_nums_list


def find_dif_frac(nums_list):
    length = len(nums_list)
    if length == 0:
        return "Список пустой."

    frac_part_list = []
    for num in nums_list:
        frac_part = round(num - int(num), 2)
        frac_part_list.append(frac_part)

    max_num = max(frac_part_list)
    min_num = min(frac_part_list)
    dif = max_num - min_num

    return f"Max: {max_num}, Min: {min_num}, Разность: {dif}"


size = int(input("Введите количество элементов в списке: "))
ls = make_list(size)

print(ls)
print(find_dif_frac(ls))

