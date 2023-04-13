# Создать файл animals.py. Создать три класса: Dog, Cat, Parrot. Атрибуты каждого класса: name, age, master. Каждый класс
# содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный метод fly. Cat - meow, Dog - bark.

class Pet:

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    @staticmethod
    def go():
        print('go!')

    def run(self):
        print(f'{self.name} running!')

    def jump(self, x):
        print(f'jump {x} m {self.name}!')

    def birthday(self):
        self.age += 1

    def sleep(self):
        print(f'{self.name} sleeping!')

    def voice(self):
        pass

    # @property
    # def height(self):
    #     return self.__height
    #
    # @height.setter
    # def height(self, new_height):
    #     self.__height = new_height
    #
    # @property
    # def weight(self):
    #     return self.__weight
    #
    # @weight.setter
    # def weight(self, new_weight):
    #     self.__weight = new_weight
    def change_weight(self, arg=None):
        if arg:
            self.weight += arg
        else:
            self.weight += 0.2

    def change_height(self, arg=None):
        if arg:
            self.height += arg
        else:
            self.height += 0.2


class Dog(Pet):

    def voice(self):
        print(f'{self.name} barking!')

    def jump(self, x):
        if x > 0.5:
            print('Dogs cannot jump so high!')
        else:
            super().jump(x)


class Cat(Pet):

    def voice(self):
        print(f'{self.name} meowing!')

    def jump(self, x):
        if x > 2:
            print('Cats cannot jump so high!')
        else:
            super().jump(x)


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def change_weight(self, arg=None):
        if arg:
            self.weight += arg
        else:
            self.weight += 0.05

    def change_height(self, arg=None):
        if arg:
            self.height += arg
        else:
            self.height += 0.05

    def fly(self):
        if self.weight > 0.1:
            print(f'This parrot {self.name} cannot fly')
        else:
            print(f'{self.name} flying!')

    def jump(self, x):
        if x > 0.05:
            print('Parrots cannot jump so high!')
        else:
            super().jump(x)

    def voice(self):
        print(f'{self.name} chik-chirik')


dog = Dog('Bobik', age=5, master='Evgeny', weight=20, height=50)
cat = Cat('Tom', age=3, master='Olya', weight=4, height=25)
parrot = Parrot('Dodik', age=2, master='Andrey', weight=3, height=30, species='AARA')
dog.jump(0.3)
cat.jump(2.1)
parrot.jump(1)
parrot.go()

# print(f'Bobik weight is {dog.weight}')
# dog.weight = 30
# print(f'Bobik new weight is {dog.weight}')
# print(f'Bobik height is {dog.height}')
# dog.height = 60
# print(f'Bobik new height is {dog.height}')
