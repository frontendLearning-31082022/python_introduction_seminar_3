# 4) Программа принимает действительное положительное число x
# и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции
# возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора возведения в степень.
# Второй — более сложная реализация без оператора возведения в степень,
# предусматривающая использование цикла.
import console_methods


def my_func(x, y):
    result_by_firstway = x ** y

    result_by_second_way = 1
    for step in range(0, y * -1):
        result_by_second_way = result_by_second_way * x

    result_by_second_way = 1 / result_by_second_way

    return result_by_second_way


if __name__ == '__main__':
    console_methods.print_console("\nInput digit positive")
    x_dig = console_methods.input_digit(positive_only=True)
    console_methods.print_console(f"\nInputed {x_dig}", True)

    console_methods.print_console("\nInput digit integer negative")
    y_dig = console_methods.input_int(negotive=True)
    console_methods.print_console(f"\nInputed {y_dig}", True)

    result = my_func(x_dig, y_dig)
    print(f"\nResult {result}")

    # print(pos_dig)
