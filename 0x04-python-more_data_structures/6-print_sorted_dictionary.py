#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ms = sorted(a_dictionary)
    for u in ms:
        print("{}: {}".format(u, a_dictionary[u]))
