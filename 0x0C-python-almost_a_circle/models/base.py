#!/usr/bin/python3
"""JSON"""
import json


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string method"""
        if (not list_dictionaries or list_dictionaries is None):
            return "[]"
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """to_json_string method"""
        if json_string in {None, ""}:
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Base class"""
        with open('{}.json'.format(cls.__name__), 'w') as f:
            objs = []
            if list_objs is not None:
                objs = list_objs

            if cls == Base:
                f.write(cls.to_json_string([vars(obj) for obj in objs]))
            else:
                f.write(cls.to_json_string(
                    [obj.to_dictionary() for obj in objs]))

    @classmethod
    def create(cls, **dictionary):
        """Base class"""
        dummy = cls(1, 2, 3, 4)
        dummy.update(**dictionary)

        return dummy
