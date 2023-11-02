#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    if len(argv[1:]) == 0:
        print("{} argument.".format(len(argv[1:])))
    else:
        print("{} argument:".format(len(argv[1:])))
    for u in range(len(argv[1:])):
        print("{}: {}".format(u + 1 , argv[u + 1]))
