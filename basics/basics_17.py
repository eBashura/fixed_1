# Рассчитать месячные выплаты (m) и суммарную выплату (s) по кредиту. О кредите известно, что он составляет n рублей,
# берется на y лет, под p процентов.  n, y, p - вводятся с клавиатуры. Месячные выплаты находятся по формуле:
# m = (n * p * (1 + p)y) / (12 * ((1 + p)y – 1)), где p выражается в долях единицы, а не процентах.
# Суммарная выплата представляет собой выплаты за все месяцы каждого года:
# s = (m * 12) * y

n = float(input('Сумма кредита = '))
y = float(input('Срок кредита = '))
p = float(input('Процентная ставка = '))
m = (n * p / 100 * (1 + p / 100) * y) / (12 * (1 + p / 100) * y - 1)
print('Ежемесячная выплата равна:', m)
s = (m * 12) * y
print('Суммарная выплата равна:', s)