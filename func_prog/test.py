from functools import reduce

arr = [3, 10, 15, 10, 5, 7, 12]

result = reduce(lambda x, y: x * y, arr)
print(result)


new_arr = list(map(lambda x: x / 2, arr))
print(new_arr)