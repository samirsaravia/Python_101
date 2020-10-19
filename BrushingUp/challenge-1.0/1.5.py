"""
Write a program that  will return the sum of the digits of an integer
"""


def sum_digit(num: int):
    string_num = str(num)
    each_val = []
    for char in string_num:
        each_val.append(int(char))
    return sum(each_val)


my_number = 78
print(f'Sum of digits of "{my_number}" is : {sum_digit(my_number)}')


def digit_sum(number):
    sum_tot = 0
    while number > 0:
        sum_tot = sum_tot + number % 10
        number = number // 10
    return sum_tot


print(f'A soma dos dígitos de 45 é: {digit_sum(45)}')
