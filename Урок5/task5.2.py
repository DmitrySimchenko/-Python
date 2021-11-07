"""Создать текстовый файл (не программно).
   Сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

"""
with open('text2.txt', 'r') as my_file:
    content = my_file.read()
    print(f'Содержимое файла: \n {content}')
with open('text2.txt', 'r') as my_file:
    lines = my_file.readlines()
    print(f'Количество строк в файле - {len(lines)}')
    for index, value in enumerate(lines):
        number_of_words = len(value.split())
        print('Строка {} содержит {} слов.'.format(index + 1, number_of_words))
