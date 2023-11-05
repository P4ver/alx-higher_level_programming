#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for u in my_list:
            if max < u:
                max = u
        return max
    else:
        return
