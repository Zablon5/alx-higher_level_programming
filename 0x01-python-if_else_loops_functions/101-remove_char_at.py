#!/usr/bin/python3
def remove_char_at(str, n):
    ans = ''
    for i, x in enumerate(str):
        if i == n:
            continue
        else:
            ans += x
    return ans        
