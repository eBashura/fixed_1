# Есть список arr = [1,2,3,4,4,4,5,5,2] while
# 4. Найти массив квадратов

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
count = 0
while count < len(arr):
    count = count ** 2
    print(count)
# import numpy
# arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
# b = list(numpy.array(arr) ** 2)
# print(b)

# arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
# count = 0
# while count < len(arr):
#     arr[count] += 1
#     print(arr[count])
