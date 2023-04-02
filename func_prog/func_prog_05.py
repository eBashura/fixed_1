# Дан список чисел. Вернуть список, где каждое число переведено в строку
# [5, 3] -> [‘5’, ‘3’]

# my_list = [5, 5, 6, 8, 9]
# my_list_2 = []
# for number in my_list:
#     new_number = str(number)
#     my_list_2.append(new_number)
# print(my_list_2)

#2 map
my_list = [5, 5, 6, 8, 9]
for i, elem in enumerate(my_list):
    my_list[i] = str(elem)
my_list_2 = list(map(str, my_list))
print(my_list_2)