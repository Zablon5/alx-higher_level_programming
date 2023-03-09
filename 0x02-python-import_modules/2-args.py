#!/usr/bin/python3
if __name__ == __"main"__:
    from sys import argv
    narg = len(argv) - 1
    if narg == 0:
        print("{} arguments.".format(narg))
    elif narg == 1:
        print("{} argument:".format(narg))
    elif narg >= 2:
        print("{} arguments:".format(narg))
    for i in range(1, narg + 1):
        print("{}: {}".format(i, argv[i]))
