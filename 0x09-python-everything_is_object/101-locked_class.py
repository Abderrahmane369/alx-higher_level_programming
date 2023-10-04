#!/usr/bin/python3
"""lockde"""


class LockedClass():
    """looooo"""
    def __setattr__(self, __name, __value) -> None:
        if __name == "first_name":
            super().__setattr__(__name, __value)

        else:
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
