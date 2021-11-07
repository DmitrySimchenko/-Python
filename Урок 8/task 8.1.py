"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.

"""


class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def transform(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31 and month == (1, 3, 5, 7, 8, 10, 12) and year > 0 \
           or 1 <= day <= 30 and month == (2, 4, 6, 9, 11) and year > 0:
            return Date.valid(day, month, year)
        else:
            return f'Ошибка ввода даты'


    def __str__(self):
        return f'Текущая дата {Date.transform(self.day_month_year)}'


today = Date('12 - 11 - 2021')
print(today)
print(Date.valid(9, 11, 2021))
print(today.valid(11, 12, 2011))
print(Date.transform('9 - 11 - 2011'))
print(today.transform('11 - 11 - 2020'))

