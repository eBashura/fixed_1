# Задан целочисленный массив. Определить количество участков массива, на котором элементы монотонно возрастают
# (каждое следующее число больше предыдущего).

from random import randint

my_list = [randint(0, 20) for el in range(40)]
print(my_list)
result = 0
count = 0
for j in range(len(my_list) - 2):
    if my_list[j + 2] > my_list[j + 1] > my_list[j]:
        count += 1
    elif count >= 1 and my_list[j + 1] > my_list[j + 2]:
        result += 1
        count = 0
if my_list[-1] > my_list[-2]:
    result += 1
print(result)

# неправильно выводит кол-во монотонных возрастаний