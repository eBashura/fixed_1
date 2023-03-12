# Введите число. Если это число делиться на 1000 без остатка, то выведите на экран "millennium"

my_num = int(input('введите число: '))
if my_num % 1000 == 0:
    print('millenium')
else:
    print('false')
