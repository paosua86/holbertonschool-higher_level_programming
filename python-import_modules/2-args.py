#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_len = len(argv)
    print("{} arguments:".format(argv_len - 1))
    for i in range(1, argv_len):
        print("{}: {}".format(i, argv[i]))
