# Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.
# Примечание: данное задание подразумевает самостоятельное изучение принципов работы со временем в Python(библиотека datetime)

trains = [
    {
        'train_num': '11',
        'place_a': 'Slutsk',
        'time_1': 7.5,
        'place_b': 'Minsk',
        'time_b': 18.5,
    },
    {
        'train_num': '10',
        'place_a': 'Slutsk',
        'time_1': 7,
        'place_b': 'Minsk',
        'time_b': 11,
    },
    {
        'train_num': '7',
        'place_a': 'Slutsk',
        'time_1': 11,
        'place_b': 'Minsk',
        'time_b': 22,
    },
    {
        'train_num': '8',
        'place_a': 'Slutsk',
        'time_1': 13.5,
        'place_b': 'Minsk',
        'time_b': 21.5
    }
]
for i in trains:
    time_v_puti = (i['time_b'] - i['time_1'])
    if time_v_puti > 7.5:
        print(f'время в пути больше 7 часов 20 минут: {i}')
    else:
        print(i, 'он быстрее чем надо')

# сырая версия задания, буду еще доделывать с time!!!




# for data in pupils:
#     print(data.items())