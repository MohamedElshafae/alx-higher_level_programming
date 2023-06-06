#!/usr/bin/python3
def remove_char_at(str, n):
    removed_str = ""
    for i in range(len(str)):
        if i == n:
            continue
        removed += str[i]
    return removed_str
