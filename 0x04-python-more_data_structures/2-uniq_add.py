#!/usr/bin/python3
def uniq_add(my_list=[]):
    neli = my_list + []
    s = 0
    for u in neli[:]:
        dl = neli.count(u)
        if dl != 1:
            neli.remove(u)
        else:
            s = s + u
    return s
