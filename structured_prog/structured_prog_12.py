# Составить список чисел Фибоначчи содержащий 15 элементов.
#
# (Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
# Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
#
# предоставить 2 решения. Одно с использованием цикла while, другое с использованием цикла for с параметром. Оба решения предоставить в одном файле.

# for
# fib1 = fib2 = 1  # 0 и 1 индексы (1 и 2 элемент списка)
# n = int(input('введите кол-во элементов: '))
# print(fib1, fib2, end=' ')
# for i in range(2, n):
#     fib3 = fib1 + fib2
#     fib1, fib2 = fib2, fib3
#     print(fib3, end=' ')
arr = [1, 1]
for i in range(13):
    arr.append(arr[-1] + arr[-2])
print(arr, len(arr))

# while
arr_2 = [1, 1]
while len(arr_2) < 15:
    arr_2.append(arr_2[-1] + arr_2[-2])
print(arr_2, len(arr_2))
