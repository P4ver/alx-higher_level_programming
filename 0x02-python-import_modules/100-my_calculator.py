#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    len_ar = len(sys.argv)
    if len_ar > 4 or len_ar < 4:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)
    elif len_ar == 4:
        ope = sys.argv[2]
        a_ar = int(sys.argv[1])
        b_ar = int(sys.argv[3])
        res = 0
        if ope == "+":
            res = calculator_1.add(a_ar, b_ar)
        elif ope == "-":
            res = calculator_1.sub(a_ar, b_ar)
        elif ope == '*':
            res = calculator_1.mul(a_ar, b_ar)
        elif ope == "/":
            res = calculator_1.div(a_ar, b_ar)
        else:
            sys.stderr.write("Unknown operator. Available operators: +, -, * and /\n")
            sys.exit(1)
        print("{} {} {} = {}".format(a_ar, ope, b_ar, res))
