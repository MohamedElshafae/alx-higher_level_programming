#!/usr/bin/python3
def pow(a, b):
    flag = 0
    if b == 0:
        return 1
    if a < 0:
        flag = 1
    if b < 0:
        for i in range(1, -b):
            a *= a
        return (1 / a)
    for i in range(1, b):
        a *= a
    if flag == 1 and b % 2 != 0:
        return -a
    return a
