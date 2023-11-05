#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        nl_a = my_list + []
        for u in range(len(my_list)):
            if u % 2 == 0:
                nl_a[u] = True
            else:
                nl_a[u] = False
        return nl_a
