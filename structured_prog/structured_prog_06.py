# Ввести строку. Если длина строки больше 10 символов, то создать новую строку с 3 восклицательными знаками в конце  ('!!!') и вывести на экран.
# Если меньше 10, то вывести на экран второй символ строки

my_str = input('введите строку: ')
if len(my_str) > 10:
    print(my_str + '!!!')
else:
    print(my_str[1])
