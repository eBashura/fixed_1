# Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.
# Примечание: данное задание подразумевает самостоятельное изучение принципов работы со временем в Python(библиотека datetime)
from datetime import datetime, timedelta

trains = [
    {
        'train_num': '11',
        'arrive': 'Slutsk',
        'arrive_time': datetime(2023, 3, 20, 19, 50),
        'start': 'Minsk',
        'start_time': datetime(2023, 3, 20, 10, 20),
    },
    {
        'train_num': '11',
        'arrive': 'Slutsk',
        'arrive_time': datetime(2023, 3, 20, 13, 40),
        'start': 'Minsk',
        'start_time': datetime(2023, 3, 20, 10, 20),
    },
    {
        'train_num': '11',
        'arrive': 'Slutsk',
        'arrive_time': datetime(2023, 3, 20, 17, 40),
        'start': 'Minsk',
        'start_time': datetime(2023, 3, 20, 10, 20),
    },
    {
        'train_num': '11',
        'arrive': 'Slutsk',
        'arrive_time': datetime(2023, 3, 20, 17, 41),
        'start': 'Minsk',
        'start_time': datetime(2023, 3, 20, 10, 20),
    }
]
timedelta_train = timedelta(hours=7, minutes=20)

for dict in trains:
    time_in_road = dict['arrive_time'] - dict['start_time']
    if time_in_road > timedelta_train:
        print(dict)



# for i in trains:
#     time_v_puti = (i['time_b'] - i['time_1'])
#     if time_v_puti > 7.5:
#         print(f'время в пути больше 7 часов 20 минут: {i}')
#     else:
#         print(i, 'он быстрее чем надо')

# сырая версия задания, буду еще доделывать с time!!!