#!/usr/bin/python3
for i in range(0, 100):
    right_digit = i % 10
    left_digit = int(i / 10) % 10
    if right_digit > left_digit:
        print("{:0d}, ".format(i), end="")
print()
