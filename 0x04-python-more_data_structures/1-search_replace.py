#!/usr/bin/python3
def search_replace(my_list, search, replace):
    hm = my_list + []
    k = 0
    for u in hm:
        if u == search:
            hm[k] = replace
        k += 1
    return hm
