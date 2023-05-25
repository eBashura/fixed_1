# Создать универсальный декоратор, который меняет порядок аргументов в функции на противоположный.
from functools import wraps


def my_decorator(func):
    # @wraps
    def inner(*args, **kwargs):
        args = args[::-1]
        kwargs = {key: value for key, value in tuple(kwargs.items())[::-1]}  # либо преобразуем в list
        return func(*args, **kwargs)

    return inner


@my_decorator
def my_func(*args, **kwargs):
    for i in args:
        print(i)
    for i in kwargs.items():
        print(i)


my_func(1, 2, 3, a=5, b=7, c=9)
