goods = []
dict_goods = []
name = []
price = []
quantity = []
unit = []
analytics = {}
number_good = 1
while input('Вы хотите добавить новый товар? (да \ нет): ') == 'да':
    dict_goods = dict({
                        'название': input('Введите название товара: '),
                       'цена': input('Введите цену товара (руб.): '),
                       'количество': input('Введите количество товара: '),
                       'ед': input('Введите единицу измерения товара: ')
                       })
    goods.append((number_good, dict_goods))
    number_good += 1

    name.append(dict_goods.get('название'))
    price.append(dict_goods.get('цена'))
    quantity.append(dict_goods.get('количество'))
    unit.append(dict_goods.get('ед'))
    analytics = {'название': name, 'цена': price, 'количество': quantity, 'ед': unit}
print('Структура данных товары: ')
for val in goods:                         # выводим в удобочитаемом виде
    print(val)
print('Структура данных аналитика: ')
for key, value in analytics.items():      # выводим в удобочитаемом виде
    print(key, ":", value)
