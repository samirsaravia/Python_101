"""
Question 2
Ask the user to input a string and then put it out to the screen
in reverse order (use a for loop)
"""
word = input('Please enter a word: ')
reverse_string = ''
for char in word:
    reverse_string = char + reverse_string
    print(reverse_string)
# print(word[::-1])
