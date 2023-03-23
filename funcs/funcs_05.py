# Создать функцию, принимающая на вход неопределенное количество аргументом и возвращающая сумму args[i] * i
# Пример:  args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10


def args_sum(*args):
    print(args, type(args))
    sum = 0
    for index, number in enumerate(args):
        sum += index * number
    return sum


def main():
    print(args_sum(2, 4, 11))


if __name__ == '__main__':
    main()
# print(f'сумма аргументов и их индексов равна: {result}')
