# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2


my_list = [1, 2, 4, 7, 10, 20, 5, 6]
my_list_new = [number * -2 for number in my_list]
print(my_list_new)
