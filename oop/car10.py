# Создать файл car10.py. Создать класс Car. Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость  - 5), стоп(сброс скорости на 0),
# отображение скорости, разворот(изменение знака скорости). Все атрибуты приватные.

class Car:
    car = 'Car'

    def __init__(self, mark, model, year, speed=0):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed

    def increase_speed(self, number=5):
        self.__speed += number

    def decrease_speed(self, number=5):
        self.__speed -= number

    def stop(self):
        self.__speed = 0

    def current_speed(self):
        return self.__speed

    @property
    def speed(self):
        return self.__speed

    def reverse_speed(self, number=-1):
        self.__speed *= number


car_1 = Car('Volvo', 'XC90', 2019)
car_2 = Car(mark='BMW', model='M5', year=2022, speed=260)
print(car_1.current_speed())
print(car_1.speed)
car_1.decrease_speed()
car_1.decrease_speed()
car_1.decrease_speed()
car_1.increase_speed()
car_1.increase_speed()
print(car_1.speed)