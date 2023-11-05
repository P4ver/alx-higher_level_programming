#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        nl_a = []
        for u in my_list:
            nl_a.append(True if u % 2 == 0 else False)
        return nl_a
