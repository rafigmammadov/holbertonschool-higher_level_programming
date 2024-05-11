#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        result = number % 10
    elif number == 0:
        result = 0
    else:
        result = -(number % 10 - 10)

    print(f"{result}", end='')

    return result
