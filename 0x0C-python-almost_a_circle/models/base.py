"""Base class"""
import json


class Base:
    """Base class (blueprint) for objrcts.
    private class attribute: __nb_objects = 0.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """init Base class.

        Args:
            id: to avoid duplicating the same code.
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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.

        Args:
            list_objs: list of instances who inherits of Base.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string.

        Args:
            json_string: string representing a list of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set.

        Args:
            **dictionary: double pointer to a dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy_instance = cls(3, 7)
            else:
                dummy_instance = cls(3)
            dummy_instance.update(**dictionary)
            return dummy_instance
