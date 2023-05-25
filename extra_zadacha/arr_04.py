# Есть список arr = [1,2,3,4,4,4,5,5,2] while
# 4. Найти массив квадратов

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
result = 0
for numbers in arr:
    result = numbers ** 2
    print('Квадратное значение числа равно', result)

# с while не получается, сделал с for

# import numpy
# arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
# b = list(numpy.array(arr) ** 2)
# print(b)
