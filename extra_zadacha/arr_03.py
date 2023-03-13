# Есть список arr = [1,2,3,4,4,4,5,5,2] while
# 3. Найти среднее геометрическое

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
count = 0
sum = 0
while count < len(arr):
    sum += arr[count] ** (1 / len(arr))
    count += 1
print(sum)

# multiple = 1 * 2 * 3 * 4 * 4 * 4 * 5 * 5 * 2
# geometric_mean = (multiple) ** (1 / len(arr))
# print(geometric_mean)


# считает неправильно, надо переделать
