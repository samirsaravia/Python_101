"""
    -*-coding = UTF-8 -*-
    author: Samir S
"""


# It looks for an item in a list(stack) position by position until
# it reaches the end of the list.


def linear_search(item, my_list):
    """
        Searching position by position
    :param item: the number to look for
    :param my_list: a list of integers
    :return: either True or False if the item is in the list or not.
    """
    found = False

    for i in range(len(my_list)):
        if item == my_list[i]:
            found = True
    return found


test = [1, 5, 4, 6, 2, 3]
print(linear_search(7, test))  # It should return False
