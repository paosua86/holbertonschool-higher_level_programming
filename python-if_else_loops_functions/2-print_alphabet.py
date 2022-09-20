#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberLast = number % 10
print ("Last digit of" )
if numberLast > 5:
    print(f"{number}, is {numberLast} and is grater than 5")
elif numberLast == 0:
    print(f"{number}, is {numberLast} and is 0")
else:
    print(f"{number}, is {numberLast} and is less than 6 and not 0")
