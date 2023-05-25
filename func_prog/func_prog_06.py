# Дан список имен, отфильтровать все имена, где есть буква o
# [‘Kate’, ‘Kolya’, ‘Alex’] -> [‘Kolya’]

name_list = ['Evgeny', 'Sanyok', 'Olya', 'Anrdeo', 'Antonio']
new_name_list = []
for name in name_list:
    if 'o' in name:
        new_name_list.append(name)
print(new_name_list)

# new_name_list = list(filter(lambda x: 'o' in x, name_list))
#
#
# def name_func(x):
#     return 'o' in x
#
#
# new_arr = list(filter(name_func, name_list))
# print(new_arr)
