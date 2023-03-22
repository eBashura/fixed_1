# Создать функцию, которая принимает на вход неопределенное количество аргументов и возвращает их сумму и максимальное из них.

def args_sum(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
        max_argument = max(args)
    return sum, max_argument


sum, max_argument = args_sum(2, 4, 11)
print(f'сумма аргументов равна: {sum}')
print(f'максимальный аргумент равен: {max_argument}')
