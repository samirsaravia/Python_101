"""
Question 4
Go to Python module web page and find a module that you like.
Play with it, read te documentation and try to implement it.
"""
import urllib.request
from time import sleep
from webbrowser import open

# import datetime
# today = datetime.date.today()
# print(f'Today it\'s {today} ')
# holiday = datetime.date(2020, 12, 25)
# delta = holiday - today
# print(f'Just {delta.days} days until the holiday')

print('checking url out'.upper())
print('==' * 10)
try:
    sleep(2)
    response = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('There is no Internet')
except Exception as error:
    print(f'There is an error {error.__class__}')
else:
    print('Success opening url')
    user_input = input('would you like I display the web page: ').strip().lower()[0]
    while user_input not in 'YySsNn':
        print('There is an error')
        user_input = input('Try again: ').strip()[0]
    if user_input in 'ys':
        print('Loading...')
        sleep(2)
        open('http://pudim.com.br/')
    else:
        print('Thanks for visiting us')
