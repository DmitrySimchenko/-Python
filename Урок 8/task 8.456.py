"""4.	Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).

Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

"""


class Warehouse:

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_wh = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'название {self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите название товара: ')
            unit_p = int(input(f'Введите цену за ед. товара: '))
            unit_q = int(input(f'Введите количество товара: '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_wh.append(self.my_unit)
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q':
            print(f'Весь склад -\n {self.my_wh}')
            return f'Выход'
        else:
            return Warehouse.reception(self)


class Printer(Warehouse):
    def __init__(self, name, price, quantity, number_of_lists):
        super().__init__('Принтер', price, quantity, number_of_lists)


class Fax(Warehouse):
    def __init__(self, name, price, quantity, number_of_lists):
        super().__init__('Факс', price, quantity, number_of_lists)


unit_1 = Printer('Canon', 2800, 2, 3)
unit_2 = Fax('Ritm', 1000, 2, 1)
print(unit_1.reception())
print(unit_2.reception())

