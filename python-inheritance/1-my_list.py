#!/usr/bin/python3
"""
Module that contains MyList class
"""


class MyList(list):
    """
    Class that contains print_sorted() method
    """
    def print_sorted(self):
        """
        Function that prints the list, but sorted (ascending sort)
        """
        sorted_list = self[:]

        for i in range(len(sorted_list)):
            for k in range(len(sorted_list) - 1 - i):
                if sorted_list[k] > sorted_list[k + 1]:
                    sorted_list[k] = sorted_list[k + 1]
                    sorted_list[k + 1] = sorted_list[k]

        print(sorted_list)
