# Создать файл animals_hierarchy.py. Реализовать следующую структуру:

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


class Pet(Animal, ABC):
    @abstractmethod
    def voice(self):
        print(f'Pet have voice!')


class WildAnimal(Animal, ABC):
    @abstractmethod
    def jump(self):
        print(f'WildAnimal is jumping!')


class Feline(ABC):
    @abstractmethod
    def scratching(self):
        raise NotImplementedError


class Canine(ABC):
    @abstractmethod
    def voet_na_lyny(self):
        raise NotImplementedError


class Cat(Pet, Feline):
    def run(self):
        print(f'Cat is running!')

    def myrkaet(self):
        print('Cat myrkaet!')

    def scratching(self):
        print(f'Cat scratching!')


class Dog(Pet, Canine):
    def bark(self):
        print(f'Dog is barking!')

    def korm(self):
        print(f'Dog eating!')

    def voet_na_lyny(self):
        print(f'Dog voet na lyny!')


class Lion(WildAnimal, Feline):
    def rawrs(self):
        print(f'Lion rawrs!')

    def sleep(self):
        print(f'Lion is sleeping!')

    def scratching(self):
        print(f'Lion scratching!')


class Wolf(WildAnimal, Canine):
    def hunt(self):
        print(f'Wolf is hunting!')

    def moet_sebya(self):
        print(f'Wolf moet sebya!')

    def voet_na_lyny(self):
        print(f'Dog voet na lyny!')
