"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

 """


def summary():
    try:
        with open('file_5.txt', 'w') as my_file:
            line = input('Введите числа через пробел: ')
            my_file.writelines(line)
            numb = line.split()
            print(sum(map(int, numb)))
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


summary()
