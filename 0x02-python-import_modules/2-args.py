#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv[1:]) == 0:
        print("{} argument.".format(len(sys.argv[1:])))
    else:
        print("{} argument:".format(len(sys.argv[1:])))
    for u in range(len(sys.argv[1:])):
        print("{}: {}".format(u + 1 , sys.argv[u + 1]))
