# Дан список целых чисел. Подсчитать сколько четных чисел в списке

my_list = [1, 2, 4, 7, 10, 20, 5, 6]
n = len(my_list)  # кол-во в строке
# print(n)
num = i = 0  # кол-во четных
# print(i)
while i < n:
    num += (my_list[i] + 1) % 2
    i += 1
print(num)

count = 0
for i in my_list:
    if i % 2 == 0:
        count += 1
print(f'count = {count}')