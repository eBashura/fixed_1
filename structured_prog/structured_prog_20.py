# В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы.

my_str = list(input('введите строку: ').split())
print(*my_str[::-1])


# my_new_str = 'hi world i am a programmer'
# my_list = my_new_str.split()
# print(my_list)
# my_list.reverse()
# print(my_list)
# new_str = ' '.join(my_list)
# print(new_str)