#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    su = 0
    larg = len(argv) - 1
    if larg > 0:
        for i in range(1, larg + 1):
            su += int(argv[i])
    print("{}".format(su))
