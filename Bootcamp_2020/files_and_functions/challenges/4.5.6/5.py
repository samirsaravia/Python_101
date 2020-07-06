"""
Question 5
Write some code that requests the user to input another capital city. Add that city to the cities in capitals.
Then print the file to the screen.
"""

user_input = input('Add a city (capital) >>> ').strip().capitalize()
while user_input.capitalize().isdigit() or user_input == '':
    print('There is an error. Please check it up.')
    user_input = input('Try again >>> ').capitalize()


file = open('capitals.txt', 'a')
file.write(f'{user_input}, ')
file.close()
with open('capitals.txt', 'r') as file:
    print(file.readline())
# dublin, amsterdam, vienna , warsaw , zagreb are cities added from user_input
