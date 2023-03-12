# Получить сумму кубов натуральных чисел от n до m, используя цикл for

n = int(input('введите число n:'))
m = int(input('введите число m:'))
my_sum = 0
for i in range(n, m + 1):
    my_sum += i ** 3
print(my_sum)

