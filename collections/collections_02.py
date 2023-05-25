# Создать список произвольного содержания. После каждой операции выводить список на экран
# Добавить к нему строку “Hello”.
# Удалить первый элемент.
# Поменять второй элемент на строку “World”.
# Удалить элемент “World”
# Вывести на экран перевернутый список

my_list = [1, 34, 'evgenyBashura', '+-', 9999]
print(my_list)

my_list.append("Hello")
print(my_list)

my_list.remove(1)
print(my_list)

my_list[1] = 'World'
print(my_list)

my_list.pop(1)
print(my_list)

my_list.reverse()
print(my_list)
