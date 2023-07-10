#!/usr/bin/python3
"""Class MyList"""


class MyList(list):
    """ class that inheret from list"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
