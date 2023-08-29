#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for val in range(x):
            print(my_list[val],end='')
        return x
    except IndexError:
        count=0
        for val in my_list:
            count+=1
            print(val,end='')
        return count

