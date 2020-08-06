"""
    -*- coding: UTF-8 -*-
    author: Samir S.
"""


# tower of Hanoi
# There are 3 stacks (towers) A,B,C
# When moving 3 disks from A to C we move the top two disks to B and then
# the bottom disk to C. More generally, when moving n disks from A to C
# we move n-1 disks to B; we then move the base disk from A to C and
# then move the stack of n-1 on B to C.


def tower_of_hanoi(a, b, c, n):
    """
        Calculate how many times it takes to move from A-stack to C
    a,b,c are the towers of hanoi or stacks
    :return: how many times it took to move all numbers in A list to C
    """

    global count
    if n == 1:
        disk = a.pop()
        c.append(disk)
        count += 1
    else:

        tower_of_hanoi(a, c, b,
                       n - 1)  # it moves top-disk(n-1) from A to B

        tower_of_hanoi(a, b, c,
                       1)  # It moves the base-disk(1) from A to C

        tower_of_hanoi(b, a, c,
                       n - 1)  # It moves the top-disk(n-1) from B to C
    return count


count = 0
A = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
B = []
C = []

print(tower_of_hanoi(A, B, C, 14))
# it should display (2**14 - 1) = 16383
