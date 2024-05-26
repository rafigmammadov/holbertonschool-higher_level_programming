#!/usr/bin/python3
"""
Documentation for module that defines Singly Linked List
"""


class Node:

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class that represents a little implementation of Singly Linked List
    """

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        node = Node(value)

        if self.head is None or self.head.data > node.data:
            node.next_node = self.head
            self.head = node
        else:
            left_pt = self.head

            while (left_pt.next_node is not None
                    and left_pt.next_node.data < node.data):
                left_pt = left_pt.next_node
            node.next_node = left_pt.next_node
            left_pt.next_node = node

    def __str__(self):
        result = []
        pointer = self.head

        while pointer is not None:
            result.append(str(pointer.data))
            pointer = pointer.next_node

        return "\n".join(result)
