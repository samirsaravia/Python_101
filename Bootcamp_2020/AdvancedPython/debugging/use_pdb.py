import pdb


def add(L):
    """ Adds the integer items of a list"""
    size = len(L)
    total = 0
    iterator = 0
    # use python debugger to trace bugs line by line
    pdb.set_trace()
    while iterator < size:
        total = total + L[iterator]
        iterator += 1
    return total


my_string = [1, 2, 3, 4, 'eight']
print(add(my_string))
