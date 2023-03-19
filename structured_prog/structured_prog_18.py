# Задан целочисленный массив. Определить количество участков массива, на котором элементы монотонно возрастают
# (каждое следующее число больше предыдущего).

from random import randint

my_list = []
a = 0
while a < 10:
    my_list.append(randint(1, 100))
    a += 1
print(my_list)
result = 0
for a in range(len(my_list) - 1):
    if my_list[a] < my_list[a + 1]:
        result += 1
print(result)
