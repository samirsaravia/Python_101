"""
Question 2
Write a function that performs multiplication of two arguments .
By default the function should multiply the first argument by two.Call it multiply
"""


def multiply(num_1, num_2=2):
    """
    :return: returns the product of num_1 and num_2 if none parameter for num_2 , it is multiply by 2
    """
    return num_1 * num_2


print(f'Inputting 34 gives {multiply(34)}')
print(f'Inputting 34 * 3 gives {multiply(34, 3)}')
