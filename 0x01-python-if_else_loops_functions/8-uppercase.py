#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        m = ord(str[i])
        h = ord(str[i]) - 32
        if m <= 90:
            var = str[i]
        else:
            var = chr(h)
        print("{}".format(var), end="")
    print("")
