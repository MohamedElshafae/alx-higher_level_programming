#!/usr/bin/python3
"""define class"""


class Square:
    """represent"""

    def __init__(self, size):
        """inti

        Args:
            size: size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
