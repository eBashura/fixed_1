# В массиве целых чисел с количеством элементов 19 определить максимальное число и заменить им все четные по значению элементы.

from random import randint

my_list = []
a = 0
while a < 19:
    my_list.append(randint(1, 100))
    a += 1
print(my_list)
max_num = max(my_list)
print(f'макс число равно: {max_num}')

# 1й способ
for a in range(len(my_list)):
    if my_list[a] % 2 == 0:
        my_list[a] = max_num
print(my_list)

# 2й способ
# for index, number in enumerate(my_list):
#     if number % 2 == 0:
#         my_list[index] = max_num
# print(my_list)
