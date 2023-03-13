# Написать игру. Пользователь должен угадать число. Сперва вводится диапазон угадывания. После колличество попыток.
# В случае правильного ответа - выводить You are the winner. В случае неправильного давать игроку подсказку
# (больше или меньше искомое число). Если за указанное количество попыток число не угадано - выводить: You are the loser и правильное число.

from random import randint

my_attempts = int(input('введите число попыток: '))
hidden_number = randint(1, 10)

for i in range(my_attempts):
    number = int(input("введите загаданное число: "))
    if number == hidden_number:
        print('You are the winner')
        break
    if number > hidden_number:
        print('искомое число меньше')
    if number < hidden_number:
        print('искомое число больше')
else:
    print(f'You are the loser. Загаданное число {hidden_number}')

# разобраться как вводить диапазон и чтобы искало в нем