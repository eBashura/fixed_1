arr = [8, 1, 2, 15, 3, 4, 4, 4, 5, 5, 2, 6]

for i in range(len(arr)): # по кол-ву элементов списка (от 0 до конца списка, не включ последний элемент)
    for j in range(i, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)

# отсортировать список с помощью функции WHILE
