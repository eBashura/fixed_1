# Создать пустой класс Dog

class Dog:
    pet = 'dog'

    def __init__(self, name, height, weight, age, master, adress='Minsk'):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__age = age
        self.__master = master
        self.__adress = adress


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, new_master):
        self.__master = new_master


    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, new_adress):
        self.__adress = new_adress


    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def bark(self):
        print(f'Bark from {self.__name}')

    # def get_adress(self):
    #     return self.__adress
    #
    # def set_adress(self, adress):
    #     return self.__adress == adress


dog_1 = Dog(name='Bobik', height=150, weight=15, age=7, master='Boris')
dog_2 = Dog(name='Tolik', height=165, weight=20, age=8, master='Andrey')

print(dog_1.__dict__)
dog_1.bark()
# print(dog_1._Dog__master)
print(f'Bobik height is {dog_1.height}')
dog_1.height = 50
print(f'Bobik new height is {dog_1.height}')
print(f'Bobik weight is {dog_1.weight}')
dog_1.weight = 30
print(f'Bobik new weight is {dog_1.weight}')
print(f'Bobik age is {dog_1.age}')
dog_1.age = 15
print(f'Bobik new age is {dog_1.age}')
# dog_1.run()
# print(dog_2.height)
# dog_2.run()
# print(dog_1.weight)
# dog_1.jump()
# print(dog_2.weight)
# dog_2.jump()
# print(dog_1.age)
# dog_1.bark()
# print(dog_2.age)
