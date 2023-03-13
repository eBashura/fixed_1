arr = [8, 1, 2, 15]

# for i in range(len(arr)): # по кол-ву элементов списка (от 0 до конца списка, не включ последний элемент)
#     for j in range(i, len(arr)):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# print(arr)

# отсортировать список с помощью функции WHILE

swapped = True
while swapped:
    swapped = False
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            # Меняем элементы
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
print(arr)
