# 6) Реализовать функцию int_func(), принимающую слово из маленьких
# латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв
# в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(lower_case_word):
    if not lower_case_word.islower():
        print(f"App prefer lower case all characters words")
    return lower_case_word.capitalize()


if __name__ == '__main__':
    print(f"Auto-inputing word in_lower_case")
    result = int_func("in_lower_case")
    print(f"Result {result}")

    special_symbol = "q"

    print(f"Input words by space separator in lower case "
          f"to get first character in upper case each one "
          f"To exit enter spec symbol - {special_symbol}")
    result = 0
    while (True):
        one_line = input()
        if one_line.__eq__("q"):
            print("App stopping")
            exit(1)

        inputed_args = one_line.split(" ")
        iterator = 0
        for word in inputed_args:
            inputed_args[iterator] = int_func(word)
            iterator += 1

        result = " ".join(inputed_args)
        print(f"Maked upper case - {result}" +
              f"\nTo exit enter spec symbol - {special_symbol}")
