"""
Write a function to add two positive integers together without using the
'+' operator.
https://en.wikipedia.org/wiki/Bitwise_operation
Explanation: https://stackoverflow.com/questions/17342042/why-this-code-for-additionusing-bitwise-operation-works-in-java

"""


def no_plus_sign(a: int, b: int):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


print(no_plus_sign(1, 4))
