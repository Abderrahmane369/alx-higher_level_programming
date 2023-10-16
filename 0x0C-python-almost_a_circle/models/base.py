#!/usr/bin/python3
"""Base class"""
import json


class Base():
    """Base class (blueprint) for objrcts.
    private class attribute: __nb_objects = 0.
    """

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """initialize Base class.

        Args:
            id: to avoid duplicating the same object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries: list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string.

        Args:
            json_string: string representing a list of dictionaries.
        """
        if json_string in {None, ""}:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.

        Args:
            list_objs: list of instances who inherits of Base class.
        """
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
        """returns an instance with all attributes already set.

        Args:
            **dictionary: double pointer to a dictionary.
        """
        dummy = cls(1, 2, 3, 4)
        dummy.update(**dictionary)

        return dummy
