"""Создать текстовый файл (не программно).
   Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
   Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
   Выполнить подсчёт средней величины дохода сотрудников.
   Пример файла:
   Иванов 23543.12
   Петров 13749.32

"""
summa = 0
count = 0
persons = []

with open('text3.txt', 'r', encoding='utf-8') as my_file:
    title = my_file.readline()

    for line in my_file.readlines():
        print(line)
        line = line.rstrip('\n')
        surname, salary = line.split(': ')
        summa += int(salary[0:])
        count += 1
        if int(salary) < 20000:
            persons.append(surname)
    print(f'Средняя величина оклада составляет: ', summa/count)
    print(f'Список сотрудников с окладом меньше 20000: ', persons)
