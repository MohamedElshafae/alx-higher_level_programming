#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers."""
    list = sorted(list_of_integers)
    if len(list) == 0:
        return None
    return list[-1]
