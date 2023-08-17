#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set12 = set_1 | set_2
    result_set = set(filter(lambda i: i not in set_1 or i not in set_2, set12))
    return (result_set)