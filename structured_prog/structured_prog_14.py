# Дано число. Найти сумму и произведение его цифр.

my_number = input('Введите число: ')
my_number_1 = str(my_number)
my_sum = 0
my_multiple = 1
for i in my_number_1:
    print(int(i))
    my_sum += int(i)
    my_multiple *= int(i)
print(f'Сумма цифр равна: {my_sum}')
print(f'Произведение цифр равно: {my_multiple}')
