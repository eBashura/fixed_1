# Ввести число, проверить на то, что было введено именно число. Возвести его в куб и вывести результат на экран.

my_number = input(f'Введите число: ')
print(type(my_number))
print(my_number.isdigit())
if my_number.isdigit():
    my_number = float(my_number)
    result = my_number ** 3
    print(result)
else:
    print("incorrect")

# if my_number is int:
#     print(my_number ** 3)
# else:
#     print("ошибка, введите число")

# my_str = input('Введите имя: ')
# if my_str == 'Борис':
#     print("Привет, Борис")
# else:
#     print("Я не знаю тебя")
