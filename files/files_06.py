# Имеются два текстовых файла с одинаковым числом строк. Выяснить, совпадают ли их строки. Если нет,
# то получить номер первой строки, в которой эти файлы отличаются друг от друга.

with open("/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie6(1)", "r") as file_1, open(
        "/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie6(2)", "r") as file_2:
    counter = 0
    flag = True
    for str_1, str_2 in zip(file_1, file_2):
        counter += 1
        if str_1 != str_2:
            flag = False
            break
print(f"Нет отличий") if flag else print(f"Отличается строка {counter}")

# zip нашел в интернете данный способ, т.к. из презы не нашел ничего полезного