# Имеются два текстовых файла с одинаковым числом строк. Выяснить, совпадают ли их строки. Если нет,
# то получить номер первой строки, в которой эти файлы отличаются друг от друга.

with open("/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie6(1)", "r") as file_1, open(
        "/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie6(2)", "r") as file_2:


# #1
#     count = 1
#     while line_1 := file_1.readline():
#         line_11 = file_2.readline()
#         if line_1 != line_11:
#             print(f'difference in {count} line')
#         count += 1
#
# #2
#     counter = 0
#     flag = True
#     for str_1, str_2 in zip(file_1, file_2):
#         counter += 1
#         if str_1 != str_2:
#             flag = False
#             break
# print(f"Нет отличий") if flag else print(f"Отличается строка {counter}")
#
# #3
#     for index, (line_1, line_2) in enumerate(zip(file_1, file_2)):
#         if line_1 != line_2:
#             print(f'difference in {index + 1} line')
#             break
