# Есть список arr = [1,2,3,4,4,4,5,5,2] while
# 1. Найти сумму всех числел
# 2. Найти среднее арифметическое
# 3. Найти среднее геомнтрическое
# 4. Найти массив квадратов
# 5*. Найти кумулятивную сумму
# 6*. Найти медиану
# 7*. Найти верхнюю и нижнюю квартиль

# arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
# count = 0
# sum = 0
# while count < len(arr):
#     sum += arr[count]
#     count += 1
# print(sum)

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
arr.sort()
print(arr)
index_v_dkvar = 0.75 * (len(arr) - 1)
int_index = int(index_v_dkvar)
if index_v_dkvar % 1:
    print(arr[int_index])
else:
    result = (arr[int_index] + arr[int_index + 1]) / 2
    print(result)


# print(sum(arr))
#
# avg = sum(arr) / len(arr)
# print(avg)
#
# multiple = 1 * 2 * 3 * 4 * 4 * 4 * 5 * 5 * 2
# geometric_mean = (multiple) ** (1 / len(arr))
# print(geometric_mean)
#
# import numpy
# start_list = [1, 2, 3, 4, 4, 4, 5, 5, 2]
# b = list(numpy.array(start_list) ** 2)
# print(b)

