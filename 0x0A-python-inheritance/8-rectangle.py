#!/usr/bin/python3
"""class rectangle inherit from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represnt Rectangle by baseGeometry"""

    def __init__(self, width, height):
        """int Rectangle

        Args:
            [width]:width of rectangle
            [height]:height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
