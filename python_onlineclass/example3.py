#!/usr/bin/python3

class Person:

    def __init__(self, i):
        self.age = i

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, i):
        if isinstance(i, int):
            self.__age = i
        else:
            print("wrong type")
            self.__age = 0

newPerson = Person("Hola Mundo")
print(newPerson.age)
print(dir(newPerson))
print(newPerson._Person__age)
print(newPerson.age is newPerson._Person__age)
