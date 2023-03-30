# from functools import reduce
#
# arr = [3, 10, 15, 10, 5, 7, 12]
#
# result = reduce(lambda x, y: x * y, arr)
# print(result)
#
#
# new_arr = list(map(lambda x: x / 2, arr))
# print(new_arr)

def my_decorator_1(func):
    def inner(*args, **kwargs):
        print('start 1 decorator')
        result = func(*args, **kwargs)
        print('finish 1 decorator')
        return result

    return inner


def my_decorator_2(func):
    def inner(*args, **kwargs):
        print('start 2 decorator')
        result = func(*args, **kwargs)
        print('finish 2 decorator')
        return result

    return inner


@my_decorator_2
@my_decorator_1 #my_func = my_decorator_2(my_decorator_1(my_func))
def my_function():
    print('very important my_func')


my_function()
