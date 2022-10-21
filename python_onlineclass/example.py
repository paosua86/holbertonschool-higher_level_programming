#!/usr/bin/python3

_Person__age = 70

class Person:
    def __str__(self):
        return "{}".format(__age)

    def hola_super(self):
        print(super())

class Kid(Person):
    __age = 12

    def __str__(self):
        return super().__str__()


_Person__age = 70

newPerson = Person()
newKid = Kid()
newPerson.hola_super()


