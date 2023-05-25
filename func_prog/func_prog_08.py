# Написать декоратор, который будет выводить время выполнения функции
# from datetime import datetime
# time = datetime.now()
# print(time)
from datetime import datetime
from functools import wraps
from time import sleep


def my_dec(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        finish_time = datetime.now()
        delta = finish_time - start_time
        print(delta)
        return result

    return inner


@my_dec
def very_important_func():
    sleep(2)
    print("very_important_func")


very_important_func()
