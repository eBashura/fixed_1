# Создать файл animals.py. Создать три класса: Dog, Cat, Parrot. Атрибуты каждого класса: name, age, master. Каждый класс
# содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный метод fly. Cat - meow, Dog - bark.

class Pet:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    @staticmethod
    def go():
        print('go!')

    def run(self):
        print(f'{self.name} running!')

    def jump(self):
        print(f'{self.name} jumping!')

    def birthday(self):
        self.age += 1

    def sleep(self):
        print(f'{self.name} sleeping!')


class Dog(Pet):

    def bark(self):
        print(f'{self.name} barking!')


class Cat(Pet):

    def meow(self):
        print(f'{self.name} meowing!')


class Parrot(Pet):

    def fly(self):
        print(f'{self.name} flying!')


dog = Dog('Bobik', age=5, master='Evgeny')
cat = Cat('Tom', age=3, master='Olya')
parrot = Parrot('Dodik', age=2, master='Andrey')
dog.jump()
cat.jump()
parrot.jump()
parrot.go()