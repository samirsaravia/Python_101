"""
Two sum function, will search for two numbers given as a target into a list.
Will return either True or False
"""


def two_sum(list_n: list, tar: int) -> bool:
    data = dict()
    for i in range(len(list_n)):
        if tar - list_n[i] in data:
            return True
        data[list_n[i]] = i
    return False


my_numbers = [x for x in range(10)]
target = 18
search = two_sum(my_numbers, target)
print(f'There are two numbers sum {target} in {my_numbers}: {search}')
