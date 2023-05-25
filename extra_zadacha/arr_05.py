# Есть список arr = [1,2,3,4,4,4,5,5,2] while
# 5*. Найти кумулятивную сумму

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
cum_sum = []
j = 0
for i in range(0, len(arr)):
    j += arr[i]
    cum_sum.append(j)
print(cum_sum)

# c while не понял как написать, поэтому использовал for
