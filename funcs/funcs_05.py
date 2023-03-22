# Создать функцию, принимающая на вход неопределенное количество аргументом и возвращающая сумму args[i] * i
# Пример:  args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10


def args_sum(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i] * i
    return sum


result = args_sum(2, 4, 11)
print(f'сумма аргументов и их индексов равна: {result}')

