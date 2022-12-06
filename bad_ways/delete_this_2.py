# 3) Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.

class Two_cells_biggest:
    def __init__(self):
        self.cells = [None, None]

    def add_value(self, value):
        if self.cells[0] == None:
            self.cells[0] = value
            return
        if self.cells[1] == None:
            self.cells[1] = value
            return

        for index in range(0, 1):
            if self.cells[index] > value:
                self.cells[index] = value
                return




def my_func(one, two, three):
    arguments = locals()

    list_numbers = []
    for vall in arguments.values():
        list_numbers.append(vall)

    sd= Two_cells_biggest()
    two_cells_biggest = Two_cells_biggest()
    while (len(list_numbers) > 0):
        cur_digit = list_numbers.pop();
        two_cells_biggest.add_value(cur_digit)


if __name__ == '__main__':
    my_func(1, 2, 3)
