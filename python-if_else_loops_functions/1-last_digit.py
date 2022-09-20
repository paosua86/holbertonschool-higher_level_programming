#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    numberLast = number % 10
else:
    numberLast = number % -10
print("Last digit of", number, "is", numberLast, end=" ")
if numberLast > 5:
    print("and is grater than 5")
elif numberLast == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
exit(0)
