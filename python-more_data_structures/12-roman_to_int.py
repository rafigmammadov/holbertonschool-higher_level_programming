#!/usr/bin/python3
def roman_to_int(roman_string):
    hash_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}

    current_value = 0
    previous_value = 0
    total_sum = 0

    if roman_string is None or isinstance(roman_string, str) is False:
        return 0

    for i in roman_string:
        current_value = hash_map[i]

        if current_value > previous_value:
            total_sum += current_value - previous_value * 2
        else:
            total_sum += current_value

        previous_value = current_value

    return total_sum
