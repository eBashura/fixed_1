# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 ->  2 3 4 5 1

# my_list = [4, 5, 6, 7, 8, 9, 10]
# new_list = my_list[1:] + my_list[:1]
# print(new_list)

# while
my_list = [4, 5, 6, 7, 8, 9, 10]
print(my_list)
arr = []
while len(my_list) > 1:
    arr.append(my_list.pop(1))
arr.append(arr.pop(0))
print(arr)

# for
my_list = [4, 5, 6, 7, 8, 9, 10]
print(my_list)
arr_2 = []
for i in range(1, len(my_list)):
    arr_2.append(my_list[i])
arr_2.append(my_list[0])
print(arr_2)





