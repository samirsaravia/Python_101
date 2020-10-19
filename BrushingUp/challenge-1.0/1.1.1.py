"""
Write a function that calculates the sum of all integers up to n.Use the
iterative method and the formula and compare the results.
(sum of n integers given by S = (n(n+1))/2)
"""


def check_sum(number: int):
    sum1 = 0
    for i in range(1, number + 1):
        print(i)
        sum1 = sum1 + i
    sum2 = number * (number + 1) / 2  # s = n*(n+1)/2
    print(sum1, sum2)


check_sum(3)
