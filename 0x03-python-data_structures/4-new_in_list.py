#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cplst = [] + my_list
    if idx < 0 or idx >= len(my_list):
        return cplst
    else:
        for e in range(len(my_list)):
            cplst[e] = my_list[e]
        cplst[idx] = element
        return cplst
