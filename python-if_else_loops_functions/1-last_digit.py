#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def remainder(number):
    if number % 10 == 0:
        return 0
    if number > 0:
        return number % 10
    else:
        return number % 10 - 10


last_digit = remainder(number)

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit}"
          " and is less than 6 and not 0")
