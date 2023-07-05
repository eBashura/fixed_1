# Создать бесконечный генератор случайных чисел.
# Использовать в генераторе временную задержку
from random import randint
from time import sleep


def create_generator():
    while True:
        yield randint(1, 100)
        sleep(1)


my_generator = create_generator()
print(my_generator)
for i in my_generator:
    print(i)
    if i == 0:
        break
