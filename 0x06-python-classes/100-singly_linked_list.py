#!/usr/bin/python3
"""eko eko eko"""


class Node():
    """ok ok ok"""
    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, _):
        if type(_) is not int:
            raise TypeError("data must be an integer")
        
        self._data = _
    
    @property
    def next_node(self):
        return self._next_node
    
    @next_node.setter
    def next_node(self, node):
        if type(node) is not Node and node is not None:
            raise TypeError("next_node must be a Node object")
        
        self._next_node = node
    
class SinglyLinkedList():
    """aaaaoeakzeaaoe"""
    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return "{}"
    
    def sorted_insert(self, _):
        head = self._head
        prev = None

        while self._head.next_node:
            if _ < self._head.next_node.data:
                self._head.next_node = Node(_, self._head.next_node)
                self._head = head


            
            self._head = self._head.next_node

