# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
# где i это порядковый номер строки в списке. Использовать генератор списков.

my_list_of_str = ['kafnakfnafk', 'faajfajgba', 'ajbgjabgajg', 'agnajgnag', 'jagjangja']

new_list = [f'{index} - {string}' for index, string in enumerate(my_list_of_str)]
print(new_list)

#second
new_arr = []
for index, value in enumerate(my_list_of_str):
    new_arr.append(f'{index} - {value}')
print(new_arr)
