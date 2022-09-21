#!/usr/bin/python3
for a in range(ord("z"), ord("a") - 1, - 1):
    print("{:c}".format((a - (ord("a") - ord("A"))) if a % 2 else a), end="")
