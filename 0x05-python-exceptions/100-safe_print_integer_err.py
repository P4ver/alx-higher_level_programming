#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as qe:
        erms_g = "Exception: {}".format(qe)
        print(erms_g, file=sys.stderr)
        return False
