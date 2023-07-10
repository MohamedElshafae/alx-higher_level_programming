#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """Represent MyInt by int"""

    def __eq__(self, other):
        """reverse behavior of =="""
        return int(self) != int(other)

    def __ne__(self, other):
        """reverse behavior of !="""
        return int(self) == int(other)
