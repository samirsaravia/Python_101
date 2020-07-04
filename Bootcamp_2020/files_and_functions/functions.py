# it's possible to return more than a single outcome
def sum_mult(a, b):
    total = a + b
    product = a * b
    return total, product


fun_call = sum_mult(3, 4)
print(fun_call)
print(type(fun_call))

# Assigning results to the variables
var_1, var_2 = sum_mult(3, 4)
# this for the first operation
print(var_1)

# this for the second operation
print(var_2)


# not a good idea using mutable list
def lengthen_list(n, my_list=[1,2,3]):
    my_list.append(n)
    return my_list


x = lengthen_list(4)
x = lengthen_list(4)
print(x)


# this is a better way using append
def lengthen_list2(n, my_list=None):
    if my_list is None:
        my_list = [1, 2, 3, n]
        # my_list.append(n)
        return my_list


y = lengthen_list2(4)
y = lengthen_list2(4)
y = lengthen_list2(4)
print(y)
