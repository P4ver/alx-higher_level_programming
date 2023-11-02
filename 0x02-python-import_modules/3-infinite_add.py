#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    summ = 0
    for u in range(1, len(sys.argv)):
        summ = summ + int(sys.argv[u])
    print("{}".format(summ))
