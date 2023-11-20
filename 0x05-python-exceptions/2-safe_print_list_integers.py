#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        cn_t = 0
        for q in range(x):
            o = my_list[q]
            if type(o) == int:
                print("{:d}".format(o), end="")
                cn_t += 1
        print()
        return cn_t
    except TypeError as e_r:
        print("TypeError", e_r)
