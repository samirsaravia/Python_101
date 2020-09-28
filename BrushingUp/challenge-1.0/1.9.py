"""
Write a function def add_commas(numbers) that will add commas to an integer
and return it as a string. for example add_commas(1000000) will return
'1,000,000' Do it first without using string formatting or f string
"""


def add_comma(number: int) -> str:
    try:
        number = int(number)
    except Exception as err:
        return f'Error {err.__class__}'
    else:
        string = str(number)
    string = string[::-1]
    new_string = ''
    for pos, char in enumerate(string):
        if pos != 0 and pos % 3 == 0:
            new_string = new_string + ','
        new_string = new_string + char
    return new_string[::-1]


my_number = 1165461231326
print(add_comma(my_number))
print(type(add_comma(my_number)))
