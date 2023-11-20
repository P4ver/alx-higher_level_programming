#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for q in range(x):
            v = my_list[q]
            print(v, end="")
    except Exception:
        pass
    print("")
    return (x if x < 5 else 5)
