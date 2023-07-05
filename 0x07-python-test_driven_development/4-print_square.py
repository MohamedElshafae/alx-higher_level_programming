#!/usr/bin/python3
"""function"""


def print_square(size):
    """..."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size <= 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print('#' * size)
