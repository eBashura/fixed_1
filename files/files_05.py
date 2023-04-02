# Имеется текстовый файл. Все четные строки этого файла записать во второй файл, а нечетные — в третий файл.
# Порядок следования строк сохраняется.

with open('/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie5(orig)') as orig_file, open(
        '/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie5(1)', 'w') as chet_file, open(
        "/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie5(2)", 'w') as nechet_file:
    lines = orig_file.readlines()
    print(lines)
    nechet_file.writelines(lines[::2])
    chet_file.writelines(lines[1::2])
