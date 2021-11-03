"""Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
   Об окончании ввода данных будет свидетельствовать пустая строка.

"""

my_f = open('text.txt', 'w')
line = input('Введите текст: ')
while line:
    my_f.write(line)
    line = input('Введите текст: \n')
    if not line:
        break
my_f.close()

my_f = open('text.txt', 'r')
content = my_f.read()
print(content)
my_f.close()
