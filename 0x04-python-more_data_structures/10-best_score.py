#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        h = list(a_dictionary.values())
        r = list(a_dictionary.keys())
        mx = 0
        for k in h:
            if mx < k:
                mx = k
        for j in r:
            if a_dictionary[j] == 16:
                return j
    else:
        return
