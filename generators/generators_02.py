# Создать бесконечный генератор случайных чисел. Генератор должен принимать диапазон случайных чисел и смещение
from random import randrange
from time import sleep


def create_generator():
    a = int(input('a = '))
    b = int(input('b = '))
    d = int(input('diff = '))
    while True:
        yield randrange(a, b, d)
        yield randrange(a + d, b + d, d)
        # yield range(a + d, b + d, d)
        sleep(1)


my_generator = create_generator()
print(my_generator)
for a, b in my_generator:
    print(f'{a} - {b}')
# пока думаю над этим, не получается
