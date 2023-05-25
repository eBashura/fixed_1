# Дан список слов. Сгенерировать новый список с перевернутыми словами

my_str = 'afasf afsa afafaa fffaf affaf aafaf fasfaf asfasfa'

my_list = my_str.split()
new_list = [i[::-1] for i in my_list]
my_new_str = ' '.join(new_list)
print(my_new_str)
#
# arr = ['afasf', 'afsa', 'afafaa', 'fffaf']
# print([i[::-1]] for i in arr)
