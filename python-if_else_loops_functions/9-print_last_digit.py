#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastNumber = (-1 * number) % 10
    else:
        lastNumber = number % 10
    print(f"{lastNumber}", end="")
    return lastNumber
