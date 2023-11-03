#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    len_ar = len(sys.argv)
    operator = ["+","-","*","/"]
    
    if len_ar == 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)
    elif sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /\n")
        exit(1)
    else:
        a_ar = int(sys.argv[1])
        b_ar = int(sys.argv[3])
        if sys.argv[2] == "+":
            res = add(a_ar, b_ar)
        elif sys.argv[2] == "-":
            res = sub(a_ar, b_ar)
        elif sys.argv[2] == "*":
            res = mul(a_ar, b_ar)
        elif sys.argv[2] == "/":
            res = div(a_ar, b_ar)
        print("{} {} {} = {}".format(a_ar, sys.argv[2], b_ar, res))
