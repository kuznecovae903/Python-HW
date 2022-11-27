# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

float_num = float(input('Enter a float number: '))
len_of_number = len(str(float_num).replace('.', ''))
#print(str(float_num).replace('.',''))
#print(len_of_number)
int_num = int(float_num * 10 ** (len_of_number - 1))
#print(int_num)
result = 0

while int_num > 0:
    remainder = int_num % 10
#    print(remainder)
    result += remainder
#    print(result)
    int_num //= 10
#    print(int_num)

print(result)