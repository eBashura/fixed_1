# Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.

my_list = [1, 20, 4, 12, 31, 3, 4, 50, 6, 7, 11]
my_sum = sum([i for i in my_list if i>=10])
print(f'сумма элементов списка, которые больше 10: {my_sum}')

# РАЗОБРАТЬСЯ КАК ПОСЧИТАТЬ СУММУ С ПОМОЩЬЮ WHILE
# my_num = 0
# my_sum = 0
#
# for i in range(my_list):
#     my_sum += my_list
#     print(my_sum)
# print('Done')

# ls=list(range(0,13))



