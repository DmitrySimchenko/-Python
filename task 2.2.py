count = int(input('Введите количество элементов списка: '))
my_list = []
for i in range(count):
    new_element = input()
    my_list.append(new_element)

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(my_list)
