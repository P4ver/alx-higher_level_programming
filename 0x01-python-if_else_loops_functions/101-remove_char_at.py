#!/usr/bin/python3
def remove_char_at(str, n):
    for h in range(len(str)):
        if h != n:
            print(str[h], end="")
    return ""
