# Создать список с фамилиями. Вывести все фамилии, которые начинаются на П и заканчиваются на а

surname_list = ['Петрова', 'Башура', 'Пушкина', 'Семенова', 'Плеханова', 'Павловко']
for i in surname_list:
    if i[0] == "П" and i[-1] == "а":
        print(i)

# 2й способ
# for i in surname_list:
#     if i.startswith('П') and i.endswith('а'):
#         print(i)
