# Создать функцию, которая принимает на вход неопределенное количество аргументов и возвращает их сумму и максимальное из них.
def summ_and_max(*args):
    return sum(args), max(args)


def main():
    result = summ_and_max(1, 2, 3, 4, 5, 6)
    print(result, type(result))
    summ, max_elem = summ_and_max(1, 2, 3, 4, 5, 6)
    print(f'сумма равна {summ}, макс значение равно {max_elem}')


if __name__ == '__main__':
    main()
# def args_sum(*args):
#     sum = 0
#     for i in range(len(args)):
#         sum += args[i]
#         max_argument = max(args)
#     return sum, max_argument
#
#
# def main():
#     print(args_sum(2, 4, 12))


# sum, max_argument = args_sum(2, 4, 11)
# print(f'сумма аргументов равна: {sum}')
# print(f'максимальный аргумент равен: {max_argument}')
