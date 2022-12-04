# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import sample

def make_list(length):
    if length <= 0:
        return []

    nums_list = sample(range(10), length)
    return nums_list


def find_sum_odd_pos(nums_list):
    length = len(nums_list)
    if length == 0:
        return "Список пустой."

    nums_sum = 0
    for i in range(len(nums_list)):
        if i % 2 != 0:
            nums_sum += nums_list[i]
    return nums_sum


size = int(input("Введите длину списка: "))
ls = make_list(size)

print(ls)
print(find_sum_odd_pos(ls))
1
# my_list = [2, 3, 5, 9, 3]
# sum = 0
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         sum += my_list[i]
# #        print(sum)
# print(sum)
