# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь.
a = 5
b = 8
c = ((a ** 2) + (b ** 2)) ** 0.5
print(f'Гипотенуза прямоугольного треугольника равна {c}')
s_trg = (a * b) / 2
print(f'Площадь прямоугольного треугольника равна {s_trg}')
