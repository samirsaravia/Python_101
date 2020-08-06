"""
    -*- coding : UTF-8 -*-
    Checking-up stack
"""


def balanced_brackets(inpt):
    over_f = str(inpt).strip()
    stack = list()
    brackets = {'{': '}', '[': ']', '(': ')'}
    for i in over_f:
        if i in brackets.keys():
            stack.append(i)
        else:
            if len(stack) == 0 or brackets[stack.pop()] != i:
                return False
    return len(stack) == 0


data = '{}{}[[(((())))]]'
print(balanced_brackets(data))
