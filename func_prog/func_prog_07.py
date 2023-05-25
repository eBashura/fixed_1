# Дан список чисел. Найти произведение всех чисел, которые кратны 3.
from functools import reduce

arr = [3, 10, 15, 10, 5, 7, 12]
new_arr = list(filter(lambda x: x % 3 == 0, arr))
# result = reduce(lambda x, y: x * y, new_arr)
# print(result)
result = 1
for i in new_arr:
    result *= i
print(new_arr)
print(f'произведение равно: {result}')

