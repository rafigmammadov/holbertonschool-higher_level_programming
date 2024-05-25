#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    max_value_key = None

    if a_dictionary is None:
        return None

    for i, j in a_dictionary.items():
        if j > max_value:
            max_value = j
            max_value_key = i
        continue

    return max_value_key
