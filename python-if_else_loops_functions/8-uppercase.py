#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in range(0, len(str)):
        if 97 <= ord(str[i]) <= 122:
            result += chr(ord(str[i]) - 32)
        else:
            result += str[i]
    print("{}\n".format(result), end='')
