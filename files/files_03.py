# В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.

# my_file = open("/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie3.txt")
with open("/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie3.txt") as my_file:
    print(my_file.read())

with open("/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie3.txt", "a") as my_file:
    for _ in range(3):
        str_add = input('print ur str - ')
        my_file.write(f'\n{str_add}')

with open("/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie3.txt") as my_file:
    print(my_file.read())

# игрался с функциями чтения
# ----------------------------
# content = my_file.readline()
# print(content)
# while True:
#     line = my_file.readline()
#     if not line:
#         break
#     print(line)

# while line := my_file.readline():
#     print(line)

# lines = my_file.readlines()
# print(lines)
#
#
# my_file.close()
