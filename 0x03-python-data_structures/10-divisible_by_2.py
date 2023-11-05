#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        nl_a = []
        u = 0
        while u < len(my_list):
            nl_a.append(True if u % 2 == 0 else False)
            u += 1
        return nl_a
