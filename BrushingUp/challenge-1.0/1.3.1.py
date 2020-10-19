"""
Write a function that takes a positive integer and converts it into hours
and minutes.
45 would return 0:45 mins, 135 would return 2h: 15mins
"""


def get_hour(number: int):
    try:
        number = int(number)
    except Exception as err:
        print(f'Error {err.__class__}')
    else:
        if number > 0:
            hour = my_n // 60
            mins = my_n % 60
            if hour > 0:
                print(f'{hour}h: {mins}min')
            else:
                print(f'{hour}:{mins}min')
        else:
            print('Error, negative value')


my_n = 135
get_hour(my_n)
