# Создать скрипт. Программа принимает имя папки и имя файла с расширением. Создает папку и создает в ней файл.
# Если расширение файла py - записывает в файл следующее:

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-dn', '--dir_name', required=True)
parser.add_argument('-fn', '--file_name', required=True)
args = parser.parse_args()
print(args)
if not os.path.isdir(args.dir_name):
    os.mkdir(args.dir_name)
try:
    with open(os.path.join(args.dir_name, args.file_name), 'a') as file:
        if args.file_name.py:
            file.write('def main(): pass if __name__ == __main__: main()')
except:
    print('Ты в чем то ошибся!')
