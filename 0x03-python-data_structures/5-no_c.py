#!/usr/bin/python3
def no_c(my_string):
    y = list(my_string)
    for u in y[:]:
        if u == 'c' or u == 'C':
            y.remove(u) 
    return "".join(y)
