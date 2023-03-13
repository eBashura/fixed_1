# Есть список arr = [1,2,3,4,4,4,5,5,2] while
# 7*. Найти верхнюю и нижнюю квартиль

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
print(arr)
print(len(arr))
index_v_dkvar = 0.75 * (len(arr) + 1)
index_n_dkvar = (len(arr) + 1) / 4
print(f'нижняя квартиль равна: {index_n_dkvar}')
print(f'верхняя квартиль равна: {index_v_dkvar}')

# arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
# arr.sort()
# print(arr)
# index_v_dkvar = 0.75 * (len(arr) - 1)
# int_index = int(index_v_dkvar)
# if index_v_dkvar % 1:
#     print(arr[int_index])
# else:
#     result = (arr[int_index] + arr[int_index + 1]) / 2
#     print(result)
