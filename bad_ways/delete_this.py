# 3) Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.


class One_entry:
    def __init__(self, key_one, key_two, value_one, value_two):
        self.key_one = key_one
        self.key_two = key_two
        self.value_one = value_one
        self.value_two = value_two

        self.sum_result = self.value_one + self.value_two

    def get_key_first(self):
        return self.key_one + self.key_two

    def get_key_swapped(self):
        return self.key_two + self.key_one


class Find_all_combinations:
    def __init__(self):
        self.dictionary_combinations = dict()

    def add(self, one_entry: One_entry):
        if self.check_already_contains(one_entry):
            return
        self.dictionary_combinations[one_entry.get_key_first()] = one_entry

    def check_already_contains(self, one_entry: One_entry):
        sum_already = False

        sum_already = self.dictionary_combinations \
            .__contains__(one_entry.get_key_first())
        sum_already = self.dictionary_combinations \
            .__contains__(one_entry.get_key_swapped())
        return sum_already


def my_func(one, two, three):
    arguments = locals()

    list_names_args = []
    for key_val in arguments.keys():
        list_names_args.append(key_val)

    uniq_sums_chains = Find_all_combinations()

    for iterator in range(0, len(list_names_args)):
        current_digit = list_names_args[iterator]

        other_part_of_list = list_names_args.copy()
        del other_part_of_list[iterator]

        while (len(other_part_of_list) > 0):
            second_digit = other_part_of_list.pop()
            one_sum_object = One_entry(key_one=current_digit,
                                       key_two=second_digit,
                                       value_one=arguments.get(current_digit),
                                       value_two=arguments.get(second_digit))
            uniq_sums_chains.add(one_sum_object)
        iterator += 1

        dsa = 0

    types_sums = None

    fsd = 0


if __name__ == '__main__':
    my_func(1, 2, 3)
