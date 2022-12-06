# Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decimal_to_binary(decimal):
    list_bins = []
    while decimal != 1:
        list_bins.append(int(decimal % 2))
        decimal = int(decimal / 2)
    list_bins.append(1)
    list_bins.reverse()
    return ''.join(map(str, list_bins))


if __name__ == '__main__':
    decimal_val = 45
    res = decimal_to_binary(decimal_val)
    print(f"Decimal {decimal_val} to binary {res}")
