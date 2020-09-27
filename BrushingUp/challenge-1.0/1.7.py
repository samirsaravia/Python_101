"""
Write a function that will check for the occurrence of double letters in a
string. If the string contains double letters next to each other it will
return true, otherwise it will return false
"""


def double_letter(word: str) -> bool:
    word = word.lower().strip()
    for pos, char in enumerate(word):
        if pos > 0:
            if char == word[pos - 1]:
                return True
    return False


my_word = 'double'
print(double_letter(my_word))
