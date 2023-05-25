# Дан словарь, создать новый словарь, поменяв местам ключ и значение

my_dict = {'a': 13, 'b': 14, 'c': 15, 'd': 16, 'e': 17}

new_dict = {value: key for key, value in my_dict.items()}

print(new_dict)

new_dict_2 = {}
for key, value in my_dict.items():
    new_dict_2[value] = key
print(new_dict_2)
