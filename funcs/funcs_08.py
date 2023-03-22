# Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое либо среднегеометрическое.
# Написать программу в виде трех функций.

def arifmet(*args, **kwargs):
    avg_arifmet = 0
    for i in args and kwargs:
        avg_arifmet += args, kwargs[i] / len(args and kwargs)
    print(avg_arifmet)


def geom(*args, **kwargs):
    avg_geom = 0
    for i in args and kwargs:
        avg_geom += args, kwargs[i] ** 1 / len(args and kwargs)
    print(avg_geom)


func_3(1, 2, 3, 4, 5, mean_type=10)

# непонятное условие задания
