# Запросить у пользователя два целых числа.
# Вывести строку вида “2 плюс 3 равно 5”
# Примечание: после ввода переменных преобразовать переменные к типу int
#  >> first_number = int(first_number)

a1 = input('Введите целое число №1: ')
print("Вы ввели:", a1)
a1 = int(a1)
b1 = input('Введите целое число №2: ')
print("Вы ввели:", b1)
b1 = int(b1)
print(f'{a1} плюс {b1} равно {sum(a1+b1)}')

print(a1 + ' плюс ' + b1 + ' равно ' + sum(a1 + b1))

# не понимаю что за ошибка выскакивает