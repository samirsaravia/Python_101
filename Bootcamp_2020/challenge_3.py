"""
Question 3
Ask the user for a number between 1 and 12 and then display a times table for that number
"""
user_input = input('Please enter a number between 1-12: ')
while (not user_input.isdigit()) or int(user_input) > 12 or int(user_input) < 0:
    print('Must be an integer between 1 and 12')
    user_input = input('Please make a selection: ')
user_input = int(user_input)
print('==' * 15)
print('This is the User Input')
print()
for i in range(1, 13):
    print(f'{user_input} X {i} = {user_input * i}')
