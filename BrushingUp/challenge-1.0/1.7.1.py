"""
Write a function that uses bitwise operations to determine whether a
number is odd or even
"""


def odd_even(number: int):
    if number & 1:
        return 'Odd'
    else:
        return 'Even'


print(odd_even(2))
