# Написать функцию по решению квадратных уравнений.

def kvadrat_uravnenie(a, b, c):
    disc = b ** 2 - 4 * a * c
    if disc < 0:
        print('нет корней')
    elif disc == 0:
        x = -b / (2 * a)
        return x
    else:
        x_1 = (-b + disc ** (1 / 2)) / (2 * a)
        x_2 = (-b - disc ** (1 / 2)) / (2 * a)
        return x_1, x_2


def main():
    x = kvadrat_uravnenie(1, 4, -5)
    print(f'x = {x}')


if __name__ == '__main__':
    main()
