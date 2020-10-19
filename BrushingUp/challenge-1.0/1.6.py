"""
Write a program that converts text into pig latin. Pig latin works as follows:
All letters before initial vowel are placed at the end of the word and then
'ay' is added (explanation adapted from wikipedia), so pig becomes igpay,
cat becomes atcay, potential becomes otentialpay etc.
"""


def pig_latin(sentence: str):
    str_form = sentence.strip().lower().split(' ')
    for word in str_form:
        first_char = word[0]
        rep = word.replace(first_char, '')
        pig_lang = rep + first_char + 'ay'
        print(pig_lang, end=' ')


def pig_l(word):
    word = word.strip()
    vowel = ['a', 'e', 'i', 'o', 'u']
    front = None
    back = None
    for index, char in enumerate(word):
        if char in vowel:
            front = word[index:]
            back = word[:index]
            break
    if not front:
        return 'No vowels'
    translation = front + back + 'ay'
    return translation


my = 'phrase '
print(pig_l(my))


my_phrase = ' any random sentence here : phrase'
pig_latin(my_phrase)
