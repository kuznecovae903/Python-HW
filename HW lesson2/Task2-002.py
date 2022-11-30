# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.
n = int(input('enter number: '))
my_list = []
for i in range(1,n+1):
    #print(my_list)
    my_list.append((1 + 1/i)**i)
    i =+1

print(my_list)
print(sum(my_list))

