#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None

    max_int = my_list[0]

    for i in my_list:
        if i > max_int:
            max_int = i
        continue

    return max_int
