# Ввести число с клавиатуры. Вернуть результат логического выражения: число больше 15 и число кратно 5.

my_num = input('Введите число: ')
my_num = int(my_num)
result = (my_num > 15) and (my_num % 5) == 0
print(result)

# if my_num > 15 and my_num % 5 == 0:
#     print('true')
# else:
#     print('false')
