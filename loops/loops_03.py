# Просуммировать неопределенное количество чисел, вводимых пользователем,
# суммировать до тех пор, пока пользователь не введёт слово «стоп»

my_sum = 0
stop_word = 'стоп'
while True:
    text = input('введите число: ')
    if text == stop_word:
        break
    number = int(text)
    my_sum += number
print(my_sum)

