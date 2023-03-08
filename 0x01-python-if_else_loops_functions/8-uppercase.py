#!/usr/bin/python3
def uppercase(str):
    for i,v in enumerate(str):
        if ord(v) >= 97 and ord(v) <= 122:
            str[i]=ord(v) - 32
    print("{}".format(str))
