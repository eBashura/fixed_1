# Создать бесконечный генератор случайных чисел. Генератор должен принимать диапазон случайных чисел и смещение
import random
from random import randrange
from time import sleep


def create_generator(a=1, b=10, d=0):
    while True:
        yield random.randint(a, b)
        sleep(1)
        a += d
        b += d


for i in create_generator(-100, 100, 10):
    print(i)
    if i == 1:
        break
