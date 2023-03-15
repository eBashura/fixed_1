# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)
#
# предоставить 2 решения. Одно с использованием цикла while, другое с использованием цикла for с параметром. Оба решения предоставить в одном файле.

my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for keys in list(my_dict):
    my_dict[keys + str(len(keys))] = my_dict.pop(keys)
print(my_dict)

# не понимаю как сделать с циклом while

# print(my_dict.keys())
# for i in my_dict.keys():
#     print(len(i))
