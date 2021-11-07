"""7.	Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.

"""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма комплексных чисел равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a + self.a * other.b} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(0, -6)
z_2 = ComplexNumber(-1, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
