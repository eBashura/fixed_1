# Запросить у пользователя возраст. Если возраст меньше 0 - вывести Wrong input,
# если меньше 18 - вывести Cola, иначе - вывести Beer

my_age = int(input('Введите ваш возраст: '))
if my_age < 0:
    print('Wrong input')
elif my_age < 18:
    print('Cola')
else:
    print('Beer')
