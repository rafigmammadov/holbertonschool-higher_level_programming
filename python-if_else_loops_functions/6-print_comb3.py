#!/usr/bin/python3
for i in range(10):
    for k in range(i + 1, 10):
        if i == 8 and k == 9:
            print("{}{}\n".format(i, k))
            break
        print("{}{}".format(i, k), end=", ")
