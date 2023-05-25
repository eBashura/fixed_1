# Дано число. Найти сумму и произведение его цифр.

# for
my_int = int(input('enter number - '))
my_int_list = list(str(my_int))
result_sum = 0
result_m = 1
for i in my_int_list:
    result_sum += int(i)
    result_m *= int(i)
print(result_sum, result_m)

# while

result_sum = 0
result_m = 1
while my_int:
    last_n = my_int % 10
    result_sum += last_n
    result_m *= last_n
    my_int //= 10
print(result_sum, result_m)