"""
Can you remember how to check if a key exists in a dictionary
Using the capitals dictionary below write some code to ask the user to input a country
,then check to see if the country is in the dictionary and if it is, print
the capital.If not tell the user it's not there.
"""

capitals = {'France': 'Paris', 'Spain': 'Madrid', 'United Kingdom': 'London', 'India': 'New Delhi',
            'Italy': 'Rome', 'Bolivia': 'Sucre', 'Brazil': 'Brasilia'}
user_input = input('Which country would you like to check:  ').strip().title()
while user_input.isdigit() or user_input == '':
    print('There is an error.')
    user_input = input('Try again: ').strip().title()
if user_input in capitals:
    print(f'The capital of {user_input} is {capitals[user_input]}')
else:
    print(f'No data available for "{user_input}"')
