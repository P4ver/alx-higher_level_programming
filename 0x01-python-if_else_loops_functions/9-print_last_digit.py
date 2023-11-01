#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        t = number % 10
    else:
        h = -1 * number
        t = h % 10
    print("{}".format(t), end="")
    return t
