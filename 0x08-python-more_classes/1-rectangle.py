#!/usr/bin/python3
""" class Rectangle """


class Rectangle:
    """representation"""

    def __init__(self, width=0, height=0):
        """init width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value
