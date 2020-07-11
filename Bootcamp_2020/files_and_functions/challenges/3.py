"""
Question 3
Write a function to calculate a to the power of b. If b is not given
its default value should be 2.Call it power
"""


def power(a, b=2):
    """
    :return: returns the power of a**b. by default b is 2
    """
    return a ** b


print(f'4 to the power of 3 gives {power(4,3)}')
print(f'Inputting 4 gives {power(4)}')
