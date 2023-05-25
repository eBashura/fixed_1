# Создать текстовый файл и записать в него 6 строк. Записываемые строки вводятся с клавиатуры.

with open('/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie2.txt', 'w') as my_file:
    for _ in range(6):
        text = input('enter str - ')
        my_file.write(text)
        my_file.write('\n')
print('---------------------------')

with open('/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie2.txt') as my_file:
    print(my_file.read())