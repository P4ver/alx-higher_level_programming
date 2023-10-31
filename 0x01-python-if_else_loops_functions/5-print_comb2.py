#!/usr/bin/python3
for n in range(0, 99):
    if n < 98:
        print("{:02}".format(n), end=", ")
    elif n == 98:
        print("{}".format(n))
