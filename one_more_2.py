# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math

if __name__ == '__main__':
    list_numbers = [2, 3, 4, 5, 6]
    # list_numbers = [2, 3, 5, 6]

    list_result = []

    for iterator in range(0, math.ceil(len(list_numbers) / 2)):
        second_index = (len(list_numbers) - 1) - iterator
        list_result.append(list_numbers[iterator] * list_numbers[second_index])

    print(f"Result {list_result}")
