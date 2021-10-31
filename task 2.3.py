month = int(input("Введите номер месяца (от 1 до 12): "))

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
if month in (1, 2, 12):
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month in (3, 4, 5):
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month in (6, 7, 8):
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif month in (9, 10, 11):
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("Такого месяца не существует")
