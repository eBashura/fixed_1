# Два натуральных числа называют дружественными, если каждое из них равно сумме всех делителей другого,
# кроме самого этого числа. Найти все пары дружественных чисел, лежащих в диапазоне от 200 до 300.

my_dict = {}
for number in range(200, 300):
    sum_d_number = 0
    for i in range(1, number):
        if number % i == 0:
            sum_d_number += i
    my_dict[number] = sum_d_number

for key in my_dict.keys():
    for value_key in my_dict.keys():
        if my_dict[key] == value_key and my_dict[value_key] == key:
            print(key)
