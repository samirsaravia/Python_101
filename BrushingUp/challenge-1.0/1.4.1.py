"""
Write a function to determine whether all numbers in a list are unique
"""

#
# def un_number(numbers: list) -> bool:
#     unique = True
#     check = []
#     for i in numbers:
#         if i in check:
#             unique = False
#         check.append(i)
#     return unique


def unique_num(numbers: list) -> bool:
    if len(numbers) == len(set(numbers)):
        return True
    else:
        return False


my_numbers = [32, 45, 1, 23, 1]
print(unique_num(my_numbers))
