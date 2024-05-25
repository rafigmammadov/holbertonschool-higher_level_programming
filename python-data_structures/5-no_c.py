#!/usr/bin/python3
def no_c(my_string):
    str_list = [i for i in my_string if i != 'C' and i != 'c']
    return ''.join(str_list)
