# Есть список arr = [1,2,3,4,4,4,5,5,2] while
# 2. Найти среднее арифметическое

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
count = 0
sum = 0
while count < len(arr):
    sum += arr[count] / len(arr)
    count += 1
print(sum)
