alphabet = 'abcdefghijklmnopqrstuvwxyz'


def shift(num):
    calc = num % len(alphabet)
    return calc


def encrypt(text, num=0):
    encrypted_message = ''
    for char in text.lower():
        look_for = alphabet.find(char)
        if char not in alphabet:
            encrypted_message += char
        else:
            encrypted_message += alphabet[shift(look_for + num)]
    return encrypted_message


message = 'Hello world!!'
print(encrypt(message, 34))
