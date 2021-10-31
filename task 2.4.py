my_str = input("Введите строку: ")

for ind, word in my_str.split(' ') and enumerate(my_str.split(' ')):
    print(ind + 1, word[0:10])

