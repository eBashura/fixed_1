# Создать пустой класс Dog

class Dog:
    pet = 'dog'

    def __init__(self, name, height, weight, age, master, adress='Minsk'):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.__master = master
        self.__adress = adress

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def bark(self):
        print(f'Bark from {self.name}')

    def change_name(self, new_name):
        self.name = new_name

    def get_master(self):
        print(self.__master)
        return self.__master

    def get_adress(self):
        return self.__adress

    def set_adress(self, adress):
        return self.__adress == adress


dog_1 = Dog(name='Bobik', height=150, weight=15, age=7, master='Boris')
dog_2 = Dog(name='Tolik', height=165, weight=20, age=8, master='Andrey')

print(dog_1.name)
dog_1.bark()
print(dog_2.name)
dog_2.bark()
print(dog_1.height)
dog_1.run()
print(dog_2.height)
dog_2.run()
print(dog_1.weight)
dog_1.jump()
print(dog_2.weight)
dog_2.jump()
print(dog_1.age)
dog_1.bark()
print(dog_2.age)
dog_2.bark()
dog_1.change_name('Nebobik')
dog_1.bark()
dog_1.get_master()
dog_2.get_master()
print(dog_2.get_adress())
dog_2.set_adress("Slutsk")  # не выводит новый адрес, который указал в set_adress
print(dog_2.get_adress())
