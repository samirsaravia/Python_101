"""
Write function that will check if  a string is a palindrome.
"""


def pal(word: str) -> print():
    word = word.lower()
    if word == word[:: -1]:
        print(f'{word.title()} IS a Palindrome')
    else:
        print(f'{word.title()} is NOT a Palindrome')


my_word = 'Hannah'
pal(my_word)
