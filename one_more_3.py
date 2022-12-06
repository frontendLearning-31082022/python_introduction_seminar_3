# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math

if __name__ == '__main__':
    list_numbers = [1.1, 1.2, 3.1, 5, 10.01]

    cut_integers = []
    for numb in list_numbers:
        cut_integers.append(numb - math.floor(numb))

    result = max(cut_integers) - min(cut_integers)
    print("Result of max " + "{:.2f}".format(max(cut_integers))
          + " and min " + "{:.2f}".format(min(cut_integers)) +
          " is " + "{:.2f}".format(result))
