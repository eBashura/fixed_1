# Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n(включая n) используя цикл while

n = int(input('введите число: '))

my_sum = 0
my_num = 1
while my_num <= n:
    my_sum += my_num ** 3
    my_num += 1
print(my_sum)
