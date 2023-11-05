#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        nl_a = my_list + []
        u = 0
        while u < len(my_list):
            if u % 2 == 0:
                nl_a[u] = True
            else:
                nl_a[u] = False
            u += 1
        return nl_a
