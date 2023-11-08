#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = list(map(lambda v: v * 2, a_dictionary.values()))
    nedict = dict(zip(a_dictionary.keys(), d))
    return nedict
