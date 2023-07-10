#!/usr/bin/python3
"""class Square that inherit from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent Square by Rectangle"""

    def __init__(self, size):
        """ init Square

        Args:
            [size]:size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return square area"""
        return self.__size ** 2
