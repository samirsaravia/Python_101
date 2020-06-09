# to get the current day , we need to use the datetime library
from datetime import datetime, timedelta
# current  now function returns the current date and time as a datetime object
current_date = datetime.now()

print('Today is ' + str(current_date))
# use timedelta to remove or add days or weeks to a date

'''
one_day = timedelta(days=1)
yesterday = current_date - one_day
print('Yesterday was ' + str(yesterday))
'''


week = timedelta(weeks=1)
last_week = current_date - week
print('Last week was ' + str(last_week))
