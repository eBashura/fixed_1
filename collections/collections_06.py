# Создать словарь произвольного содержания. После каждой операции выводить словарь на экран
# Добавить новую пару по ключу alex. Значение - 42
# Вывести на экран значение по ключу alex.
# Изменить значение по ключу alex на 55.
# Удалить элемент с ключом alex.

my_dict = {'a': 33, 'b': 99, 'c': 1111111, 'd': 9128492149314}
print(my_dict)

my_dict['alex'] = 42
print(my_dict)

print(my_dict['alex'])

my_dict['alex'] = 55
print(my_dict['alex'])

my_dict.pop('alex')
print(my_dict)


