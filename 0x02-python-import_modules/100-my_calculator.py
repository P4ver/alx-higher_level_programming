#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    len_ar = len(sys.argv)
    operator = ["+", "-", "*", "/"]
    if len_ar != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a_ar = int(sys.argv[1])
    b_ar = int(sys.argv[3])
    if sys.argv[2] == "+":
        print("{} + {} = {}".format(a_ar, b_ar, add(a_ar, b_ar)))
    elif sys.argv[2] == "-":
        print("{} - {} = {}".format(a_ar, b_ar, sub(a_ar, b_ar)))
    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(a_ar, b_ar, mul(a_ar, b_ar)))
    elif sys.argv[2] == "/":
        print("{} / {} = {}".format(a_ar, b_ar, div(a_ar, b_ar)))
