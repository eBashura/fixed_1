# Имеется текстовый файл. Переписать в другой файл все его строки с заменой в них символа 0 на символ 1 и наоборот.

with open("/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie4.txt") as old_file, open(
        "/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie4(2).txt", "w") as new_file:
    a = True
    while a:
        s = ""
        a = old_file.readline()
        for i in a:
            if i == "0":
                s += "1"
            elif i == "1":
                s += "0"
            else:
                s += i
        new_file.write(s)
