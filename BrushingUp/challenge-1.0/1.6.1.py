"""
Write a function that will calculate the number of divisors of a positive
integer and return those divisors
"""


# def check_div(number: int) -> list:
#     list_div = []
#     i = 1
#     while i != number + 1:
#         if number % i == 0:
#             list_div.append(i)
#         i += 1
#     return list_div


def divisors(number: int):
    divsr = [i for i in range(1, number + 1) if number % i == 0]
    return divsr, len(divsr)


my_number = 27
print(divisors(my_number))
