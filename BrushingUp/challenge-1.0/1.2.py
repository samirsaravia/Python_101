"""
Write a program to determine whether a given number is within 10 of 100
or 200
"""


def tenth_in_hundred(number):
    if (abs(100 - number)) <= 10 or (abs(200 - number)) <= 10:
        return True
    else:
        return False


my_number = 212
print(f'The number "{my_number}" is within 10 of 100 or 200:'
      f' {tenth_in_hundred(my_number)}')
