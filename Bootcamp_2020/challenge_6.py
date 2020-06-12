"""
Question 6
Write a code that will calculate 15 factorial.
(factorial is product of positive ints up to a given number)
"""
user_input = input('Enter a number: ')
while not user_input.isdigit():
    print('This is not an integer, numbers only.')
    user_input = input('Try again: ')
user_input = int(user_input)
fact = 1
for i in range(1, user_input + 1):
    fact = fact * i
print(f'The factorial of {user_input} is {fact}')
