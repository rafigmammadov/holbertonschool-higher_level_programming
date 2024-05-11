#!/usr/bin/python3
for i in range(10):
    for k in range(i + 1, 10):
        if i == 8 and k == 9:
            print(f"{i}{k}\n")
            break
        print(f"{i}{k}", end=", ")
