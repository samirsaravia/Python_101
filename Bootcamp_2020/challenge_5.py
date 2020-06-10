"""
Question 5
ask a user to input a sequence of numbers.
Then calculate the mean and print the results.
"""
user_input = input('Please enter a number: ').strip()
numbers = list()
while user_input.lower() != 'exit':
    while not user_input.isdigit():
        print('This is not a number. Numbers only please.')
        user_input = input('Try again: ').strip()
    user_input = int(user_input)
    numbers.append(user_input)
    user_input = input('Next number: ')
total = 0
for i in numbers:
    total += i
    print(i, end=' ')
print()
print(f'The mean is {total / len(numbers)}')
# another way to work the mean out
print(sum(numbers) / len(numbers))
print(f'The total is = {total}')
