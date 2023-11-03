#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    len_ar = len(sys.argv)
    if len_ar > 4 or len_ar < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)
    elif len_ar == 4:
        ope = sys.argv[2]
        a_ar = int(sys.argv[1])
        b_ar = int(sys.argv[3])
        res = 0
        if ope == "+":
            res = add(a_ar, b_ar)
        elif ope == "-":
            res = sub(a_ar, b_ar)
        elif ope == '*':
            res = mul(a_ar, b_ar)
        elif ope == "/":
            res = div(a_ar, b_ar)
        else:
            print("Unknown operator. Available operators: +, -, * and /\n")
            exit(1)
        print("{} {} {} = {}".format(a_ar, ope, b_ar, res))
