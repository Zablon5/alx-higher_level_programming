#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list)==0:
        return 0
    deno=0
    num=0
    for (i,j) in my_list:
        num+=(i*j)  
        deno+=j
    return num/deno      