# ДОПОЛНИТЕЛЬНО, НО НЕОБЯЗАТЕЛЬНО:
# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
#
# Написать программу, которая будет ввыводит в консоль заданный текст (Python - один из самых популярных языков программирования в мире), затем принимать из консоли шаблон подстроки и удалять в задданом тексте все слова в которых присутствует введенный шаблон
# Пример:
# Python - один из самых популярных языков программирования в мире
# Введите подстроку: ам
# Python - один из популярных языков в мире

import random
def mix_list(list_original):
    # Создаем копию, поскольку мы не должны изменять оригинал
    list = list_original[:]
    # Цикл от 0 до длины списка -1
    list_length = len(list)
    for i in range(list_length):
        # Получение случайного индекса
        index_aleatory = random.randint(0, list_length - 1)
        # Замена
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    # Возвращаем список
    return list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = mix_list(list)
print("Исходный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)