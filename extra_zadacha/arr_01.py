# Есть список arr = [1,2,3,4,4,4,5,5,2] while
# 1. Найти сумму всех числел

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
count = 0
sum = 0
while count < len(arr):
    sum += arr[count]
    count += 1
print(sum)