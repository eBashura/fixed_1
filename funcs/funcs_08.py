# Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое либо среднегеометрическое.
# Написать программу в виде трех функций.
from functools import reduce


def arifmetik(*args):
    return sum(args) / len(args)


# def geometrik(*args):
#     return reduce(lambda x, y: x * y, args) ** (1 / len(args))

def geometrik(*args):
    result = 1
    for i in args:
        result *= i
    return result ** (1 / len(args))


def result_avg(*args, mean_type):
    if mean_type == 1:
        return geometrik(*args)
    elif mean_type == 0:
        return arifmetik(*args)


def main():
    print(f' geometrik = {result_avg(3, 4, 5, mean_type=1)}')
    print(f' arifmetik = {result_avg(3, 4, 5, mean_type=0)}')


if __name__ == '__main__':
    main()