# Для каждого натурального числа в промежутке от m до n вывести все делители, кроме единицы и самого числа. m и n вводятся с клавиатуры.

m = int(input('m = '))
n = int(input('n = '))
dict = {}
x = range(m, n + 1)
for number in x:
    dict[number] = []
    for i in range(2, number):
        if number % i == 0:
            dict[number].append(i)

for i in dict.items():
    print(i)

# не выводит красиво в одну строку
