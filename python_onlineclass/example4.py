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

class Kid(Person):
    def __init__(self, i):
        super().__init__(i)

    @property
    def kid_age(self):
        return self.__age

    @kid_age.setter
    def kid_age(self, i):
        if i >= 18:
            print("Sorry, you are not a kid")
            self.__age = 0
        else:
            self.__age = i

newKid = Kid(20)
newKid.kid_age = 12
print(newKid.kid_age)
print(newKid.age)

