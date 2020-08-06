
def insertion_sort(my_list):
    """
        Sort a list out
    :param my_list: a list of integers
    :return: crescent sorted list
    """
    n = len(my_list)

    for i in range(1, n):
        value = my_list[i]
        j = i
        while j > 0 and my_list[j - 1] > value:
            my_list[j] = my_list[j - 1]
            j -= 1
        my_list[j] = value
    return my_list


test = [5, 4, 2]
print(insertion_sort(test))
