# 1) Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.
import console_methods


def division_separate(dig_1, dig_2):
    if dig_2 == 0:
        console_methods.print_console(
            "Division on zero incorrect - error app stop")
        exit(1)
    resul = dig_1 / dig_2
    return resul


if __name__ == '__main__':
    dig_1 = console_methods.input_digit(False)
    dig_2 = console_methods.input_digit(False)

    resul = division_separate(dig_1, dig_2)
    print(f"Result {resul}")
