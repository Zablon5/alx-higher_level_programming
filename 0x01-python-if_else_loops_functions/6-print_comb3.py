#!/usr/bin/python3
for j in range(0, 8):
    for i in range(j+1, 10):
        print("{}{}, ".format(j, i), end='')
print("{}{}".format(j+1, i))      
