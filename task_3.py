# 3) Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.


def my_func(one, two, three):
    arguments = locals()

    list_numbers = []
    for vall in arguments.values():
        list_numbers.append(vall)

    list_numbers = sorted(list_numbers, reverse=True)

    sum_result = list_numbers[0] + list_numbers[1]
    return sum_result


if __name__ == '__main__':
    result = my_func(1, 2, 3)
    print(f"Result on sum biggest two {result} ")

    # result = my_func(10, 2, 3)
    # print(f"Result on sum biggest two {result} ")
