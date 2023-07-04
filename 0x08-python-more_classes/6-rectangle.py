#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """representaion"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """intitwidth and geight"""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calc area"""
        return self.width * self.height

    def perimeter(self):
        """calc perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """print rect"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            string = ""
            for i in range(self.height):
                for j in range(self.width):
                    string += "#"
                if i < self.height - 1:
                    string += "\n"
            return string

    def __repr__(self):
        """..."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """..."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
