"""2.	Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = "txt"


def division(divident, divider):
    try:
        if divider == 0:
            raise OwnError("Делитель равен 0! Операция не возможна!")
        print(round(divident / divider, 2))
    except NameError:
        print('Вы ввели не число')
    except OwnError as err:
        print(err)


division(4, 0)