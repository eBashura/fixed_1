# Написать скрипт - таймер. Создать программу Pomodoro.
#
# На вход программа получает имя, фамилию, время для фокусировки(по-умолчанию 25 минут), длину перерыва(по-умолчанию 5 минут),
# количество циклов(по-умолчанию 4) и название задачи. Программа указывает оставшееся время фокусировки,
# после сигнализирует о наступлении перерыва, после сигнализирует о начале нового цикла фокусировки.
# Программа должна вести файл лога о всех запусках.

import argparse
import csv
import os
import time
from datetime import timedelta

parser = argparse.ArgumentParser()
parser.add_argument('-ln', '--last_name', required=True)
parser.add_argument('-fn', '--first_name', required=True)
parser.add_argument('-tf', '--time_fix', default=25, type=int)
parser.add_argument('-br', '--break', default=5, type=int)
parser.add_argument('-c', '--cycles', default=4, type=int)
parser.add_argument('-t', '--task')
args = parser.parse_args()
time_start = time.ctime()

if not os.path.exists('log_timer_pomodor.csv'):
    with open('log_timer.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        fields = ['first name', 'last name', 'time start', 'task']

with open('log_timer_pomodor.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    if not os.path.exists('log_timer.csv'):
        fields = ['first name', 'last name', 'time start']
        csvwriter.writerow(fields)
    csvwriter.writerow([args.first_name, args.last_name, time.ctime()])

my_timedelta = timedelta(hours=args.hours, minutes=args.minutes, seconds=args.seconds)

while my_timedelta:
    print(my_timedelta)
    my_timedelta -= timedelta(seconds=1)
    time.sleep(1)
print('ALARM!!!')

# доделать!!!
