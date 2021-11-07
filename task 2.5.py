my_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите новый элемент рейтинга: '))
i = len(my_list)
if new_el <= my_list[0]:
    while i != 0:
        if new_el <= my_list[i - 1]:   # перебираем элементы в обратном порядке
            my_list.insert(i, new_el)  # новый элемент размещаем справа от равного или большего себя
            break
        else:
            i -= 1
else:
    my_list.insert(0, new_el)
print(my_list)
