#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):  # j always starts one ahead of i
        if i == 8 and j == 9:  # Last combination
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")

