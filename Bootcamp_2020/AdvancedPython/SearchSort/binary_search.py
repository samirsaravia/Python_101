"""
    -*- coding: UTF-8 -*-
    author: Samir.
"""


# Binary-search looks for an item in a list by slicing it
# until the item either has been found or it hasn't been found.
# Binary-search is not linear


def binary_search(item, my_list):
    found = False
    first = 0
    last = len(my_list) - 1

    while first <= last and found is False:
        midpoint = (first + last) // 2
        if my_list[midpoint] == item:
            found = True
        else:
            if my_list[midpoint] < item:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found


test = [2, 7, 1, 3, 4]
print(binary_search(4, test))
