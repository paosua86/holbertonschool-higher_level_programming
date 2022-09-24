#!/bin/usr/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = ["+", "-", "*", "/"]
    from 1-calculator import add, sub, mul, div
    funcs = [add, sub, mul, div]
    for i, s in enumerate(op):
        if argv[2] == s:
            print("{} {} {} = {}".format(a, s, b, funcs[i](a, b)))
            break
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
