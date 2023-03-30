# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.

file = open('/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie1.txt')
filereader = file.read()
print(filereader)
file_list = filereader.split()
# print(file_list)
print(file_list[0], file_list[4], file_list[:5], file_list[0:2], file_list, sep='\n')
file.close()

# while line := filereader.readline():
#     print(line.strip())
# filereader.close()

file_2 = open('/home/evgeny/PycharmProjects/fixed_1/files/test_files/zadanie1.txt')
counter = 0
while line := file_2.readline():
    if counter == 0:
        print(line)
        break
file_2.close()
