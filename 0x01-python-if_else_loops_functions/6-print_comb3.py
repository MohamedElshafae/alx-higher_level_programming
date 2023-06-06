#!/usr/bin/python3
for i in range(0, 89):
    right_digit = i % 10
    left_digit = int(i / 10) % 10
    if right_digit > left_digit:
        print("{:02d}, ".format(i), end="")
print(89)
