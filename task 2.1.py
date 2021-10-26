list = [1, 'text', None, 24.23, True, (5, 6), [1, 2]]
def my_type(i):
    for i in range(len(list)):
        print(type(list[i]))
    return
my_type(list)

