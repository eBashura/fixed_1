# Просуммировать неопределенное количество чисел, вводимых пользователем, суммировать до тех пор,
# пока пользователь не введёт слово «стоп». Не учитывать числа кратные 5

count = 0
stop_word = 'stop'
while True:
    num = input('введите число: ')
    if num == stop_word:
        break
    if int(num) % 5 == 0:
        print(count)
        continue
    if num != stop_word:
        count = count + int(num)
        print(count)
print(f'сумма введенных чисел равна: {count}')

# в конце при вводе стоп выводит ошибку, разобраться почему так
