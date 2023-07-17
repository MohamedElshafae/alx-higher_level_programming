#!/usr/bin/python3
"""Class Base"""
import json


class Base:
    """represent Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init Base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert dictionary to json file"""
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        fileName = cls.__name__ + ".json"
        with open(fileName, "w") as f:
            if list_objs is None:
                json.dump([], f)
            else:
                for obj in list_objs:
                    json.dump(json.loads(cls.to_json_string(
                        (obj.to_dictionary()))), f)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            obj = Rectangle(0, 0)
        elif cls.__name__ == "Square":
            obj = Square(0)
        obj.update(**dictionary)
        return (obj)

    @classmethod
    def load_from_file(cls):
        """that returns a list of instances"""
        try:
            fileName = cls.__name__ + ".json"
            with open(fileName, "r", encoding="UTF8") as f:
                data = cls.from_json_string(f.read())
        except Exception:
            return []
        obj = []
        for i in data:
            t = cls.create(**i)
            obj.append(t)
        return obj
