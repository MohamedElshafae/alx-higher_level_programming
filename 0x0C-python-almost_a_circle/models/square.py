#!/usr/bin/python3
"""define rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represent square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init values"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """module Square size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """module Square size setter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update values"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        '''
            Returns a dictionary representation of this class
        '''
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'size': getattr(self, "size")}
