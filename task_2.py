# 2) Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
import re


# not_inputed = 'not_inputed'
# def add_user(name=not_inputed, surname=not_inputed, year=not_inputed
#              , city=not_inputed, email=not_inputed, phone_number=not_inputed):


def add_user_none(name=None, surname=None, year=None
                  , city=None, email=None, phone_number=None):
    arguments = locals()
    formatting_str = str(arguments).replace("'", "")
    formatting_str = re.sub("[{}]", "", formatting_str)
    print(formatting_str)


if __name__ == '__main__':
    add_user_none(name='Valera', surname='Somov', year='03.03.1993',
                  city='Moscow'
                  , email='g3g@mail.ru', phone_number='8800808080')

    add_user_none(city='Moscow', surname='Somov', name='Valera',
                  year='08.03.1990'
                  , email='gg2@mail.ru', phone_number='8800853080')

    add_user_none(email='g1g@mail.ru', name='Grigorii', surname='Ivanov',
                  year='10.03.1993',
                  city='Moscow'
                  , phone_number='8800708080')
