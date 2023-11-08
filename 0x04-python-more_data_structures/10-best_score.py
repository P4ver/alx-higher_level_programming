#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        h = list(a_dictionary.values())
        mx = 0
        for k in h:
            if mx < k:
                mx = k
        return mx
    else:
        return
