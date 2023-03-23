# Создать функцию, которая принимает на вход неопределенное количество именованных аргументов и выводит на экран те из них, длина ключа которых четна.

def chetnie(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(key, value)


def main():
    chetnie(abcfd=2, bbbb=5, cdfagadg=6, ababab=10)


if __name__ == '__main__':
    main()
# chetnie(abcfd=2, bbbb=5, cdfagadg=6, ababab=10)
