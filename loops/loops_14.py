# Создать список учеников подобной структуры. Определить средний балл каждого студента по всем предметам,
# и вывести сведения о студентах, средний балл которых больше 4.

pupils = [
    {
        'firstname': 'Masha',
        'group': 42,
        'physics': 7,
        'informatics': 6,
        'history': 8,
    },
    {
        'firstname': 'Sasha',
        'group': 42,
        'physics': 3,
        'informatics': 4,
        'history': 4,
    },
    {
        'firstname': 'Nikita',
        'group': 38,
        'physics': 8,
        'informatics': 8,
        'history': 6,
    },
    {
        'firstname': 'Evgeny',
        'group': 11,
        'physics': 2,
        'informatics': 10,
        'history': 5
    }
]
for i in pupils:
    avg_mark = (i['physics'] + i['informatics'] + i['history']) / 3
    if avg_mark > 4:
        print(i)
    else:
        print(i, 'он двоечник')
    print(f'средний балл равен: {avg_mark}')

# for data in pupils:
#     print(data.items())

