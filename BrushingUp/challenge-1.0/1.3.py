"""
Write a program that takes a list of non-negative integers and prints
each integer to the screen the same number of times as the value of the
integer, each new value on a new line , for example:
[2,4,1,3] would print
22
4444
1
333
"""


def rep_val(number: list) -> iter:
    for i in number:
        while True:
            try:
                if i > 0:
                    value = str(i) * i
                    print(value)
            except TypeError:
                print('Oops!! Mistyping')
                break
            except Exception as err:
                print(f'Something went wrong. {err.__class__}')
                break
            else:
                break


my_list = [x for x in range(10)]
rep_val(my_list)
