#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    narg = len(argv) - 1
    if narg < 1:
        print("{} arguments.".format(narg))
    else:
        if narg == 1:
            print("{} argument:".format(narg))
        else:
            print("{} arguments:".format(narg))
        for i in range(1, narg + 1):
            print("{}: {}".format(i, argv[i]))
