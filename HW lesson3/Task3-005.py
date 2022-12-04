# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib_negafib_nums(number):
    fib_nums_list = [1, 0, 1]
    if number == 1 or num == 2:
        return fib_nums_list

    for i in range(1, number):
        size = len(fib_nums_list) - 1
        fib = fib_nums_list[size - 1] + fib_nums_list[size]
        fib_nums_list.append(fib)
        if i % 2 == 0:
            fib_nums_list.insert(0, fib)
        else:
            fib_nums_list.insert(0, -fib)

    return fib_nums_list


num = int(input("Enter a number: "))
func = fib_negafib_nums(num)

print(*func)

#Для решения задачи с Фибоначчи
# my_list = [0]
# for i in range(1, 5):
#     my_list.append(i)
#     my_list.insert(0, -i)
# print(my_list)

