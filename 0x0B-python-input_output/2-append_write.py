#!/usr/bin/python3
"""..."""


def append_write(filename="", text=""):
    """appends text ate the end and returns the number of characters added"""
    with open(filename, mode="a", encoding='utf-8') as file:
        num_of_bytes = file.write(text)
        file.close()
        return num_of_bytes
