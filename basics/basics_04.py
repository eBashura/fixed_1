# Создать два списка a = [1,2,3,4] и b = [ ]
# Вывести на экран id a и b
# Присвоить b значение a (b=a)
# Вывести на экран id переменных
# Добавить элемент в список b
# Вывести на экран оба списка

# from copy import copy

a = [1, 2, 3, 4]
b = []
print(f'first list id = {id(a)}, second list id = {id(b)}')
b = a
print(f'first list id = {id(a)}, second list id = {id(b)}')
b.append(5)
print(a, b)

# b = copy(a)
# print(f'first list id = {id(a)}, second list id = {id(b)}')
