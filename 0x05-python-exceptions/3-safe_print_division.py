#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if b != 0:
            re_s = a / b
        else:
            re_s = "None"
        return re_s
    except ZeroDivisionError as e_r:
        pass
    finally:
        print("Inside result: {}".format(re_s))
