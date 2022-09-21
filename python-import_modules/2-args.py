#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_len = len(argv)
    if argv_len == 1:
        print("{} arguments.".format(argv_len - 1))
    elif argv_len == 2:
        print("{} argument:".format(argv_len - 1))
    else:
        print("{} arguments:".format(argv_len - 1))
    for i in range(1, argv_len):
        print("{}: {}".format(i, argv[i]))
