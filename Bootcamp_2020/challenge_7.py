"""
Question 7
Write code to calculate fibonacci numbers, create lists containing first 20 fibonacci numbers.
(Fib numbers made by sum of proceeding two.Series start at 0 1 1 2 3 5 8 13...)
"""
a = 0
b = 1
fib_num = list()
count = 0
user_input = input('Enter a number: ')
while not user_input.isdigit():
    user_input = input('Try again: ')
user_input = int(user_input)
while count != user_input:
    count += 1
    fib_num.append(a)
    a, b = b, a + b
print(fib_num)
