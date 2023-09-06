#!/usr/bin/python3
def magic_string(call = [0]):
    call[0] += 1
    return ("BestSchool" + ", Best School" * (call[0] - 1))
