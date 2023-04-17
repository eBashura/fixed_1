import csv


def create(name, fields: list, rows: list):
    with open(name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


def reading(name):
    with open(name, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        result = []
        for row in csvreader:
            result.append(row)
    return result


def writing(name, rows):
    with open(name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)


def adding(name, row, index=-1):
    if index == -1:
        with open(name, "a") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row)
    else:
        rows = reading(name)
        rows.insert(index, row)
        writing(name, rows)


def deleting(name, index=-1):
    rows = reading(name)
    rows.pop(index)
    writing(name, rows)


def summ(name):
    rows = reading(name)
    summ = 0
    for row in rows[1:]:
        summ += float(row[1]) * float(row[2])
    # summa = sum([float(row[1]) * float(row[2]) for row in rows[1:]])
    return summ


def max_price(name):
    rows = reading(name)
    max_price = max([float(row[1]) for row in rows[1:]])
    index_max = [i for i, row in enumerate(rows[1:]) if max_price == float(row[1])]
    return max_price, index_max


def min_price(name):
    rows = reading(name)
    min_price = min([float(row[1]) for row in rows[1:]])
    index_min = [i for i, row in enumerate(rows[1:])
                 if min_price == float(row[1])]
    return min_price, index_min


def minus(name, row, n=1):
    rows = reading(name)
    rows[row][2] = float(rows[row][2]) - n
    writing(name, rows)
