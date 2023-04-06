# Создать csv файл с данными следующей структуры: Имя, Фамилия, Возраст.
# Создать отчетный файл с информацией по количеству людей входящих в ту или иную возрастную группу.
# Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.

import csv

rows = [
    ['firstname', 'lastname', 'age'],
    ['Evgeny', 'Bashura', '22'],
    ['Andrei', 'Andreev', '24'],
    ['Anton', 'Antonov', '29'],
    ['Sergey', 'Bashura', '35']
]
with open('test_files/csv_1.csv', 'w') as csvfile:
    csv_write = csv.writer(csvfile)
    csv_write.writerows(rows)

dict_name = {'1-12': 0, '13-18': 0, '19-25': 0, '26-40': 0, '40+': 0}
with open('test_files/csv_1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    rows = [row for row in csvreader]
    for row in rows[1:]:
        print(row)
        age = int(row[2])
        if age < 13:
            dict_name['1-12'] += 1
        elif age < 19:
            dict_name['13-18'] += 1
        elif age < 26:
            dict_name['19-25'] += 1
        elif age < 41:
            dict_name['26-40'] += 1
        else:
            dict_name['40+'] += 1
fieldnames = ['1-12', '13-18', '19-25', '26-40', '40+']

with open('/home/evgeny/PycharmProjects/fixed_1/files/test_files/csv_1_result.csv', 'w') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader()
    csvwriter.writerow(dict_name)

with open('/home/evgeny/PycharmProjects/fixed_1/files/test_files/csv_1_result.csv', 'r') as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:
        print(row)

with open('/home/evgeny/PycharmProjects/fixed_1/files/test_files/csv_1_result.csv', 'r') as file:
    csvreader = csv.reader(file)
    rows = [row for row in csvreader]
    print(rows)
