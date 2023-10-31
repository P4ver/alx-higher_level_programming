#!/usr/bin/python3
for n in range(0, 9):
    for h in range (n + 1, 10):
        if n < 8:
            print("{}{}".format(n, h), end=", ")
        elif n == 8 and h == 9:
            print("{}{}".format(n, h))
