# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input('Введите номер четверти: '))
if num == 1:
    print('Четверть I: x > 0; y > 0')
elif num == 2:
    print('Четверть II: x > 0; y < 0')
elif num == 3:
    print('Четверть III: x < 0; y < 0')
elif num == 4:
    print('Четверть IV: x < 0; y > 0')
else:
    print('Вы ввели некорректное значение')