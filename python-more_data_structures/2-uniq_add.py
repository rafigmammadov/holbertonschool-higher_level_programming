#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list_set = set(my_list)
    total_sum = 0

    for i in my_list_set:
        total_sum += i

    return total_sum
