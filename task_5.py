# 5) Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом
# и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
# подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после
# нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.
import re


def is_it_num_input(inputed):
    result = re.findall(r'\D', inputed)
    result = list(filter(lambda x: not (str(x).__eq__("-")), result))
    result = list(filter(lambda x: not (str(x).__eq__(".")), result))

    bool = corrected_input = len(result) == 0
    return bool


if __name__ == '__main__':
    special_symbol = "q"

    print(f"Input numbers by space separator. Enter - get sum all. "
          f"To exit enter spec symbol - {special_symbol}")
    result = 0
    while (True):
        one_line = input()
        inputed_args = one_line.split(" ")
        for string_val in inputed_args:
            if is_it_num_input(string_val):
                result = result + float(string_val)
            if string_val.__eq__("q"):
                print(f"Last Sum {result} ")
                print("App stopping")
                exit(1)
        print(f"Sum {result} "
              f"(Exit - enter spec symbol - {special_symbol})")
