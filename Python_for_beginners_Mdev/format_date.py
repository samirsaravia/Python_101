from datetime import datetime

today = datetime.now()
print('Today is ' + str(today))

# use date, month, year, hour , minutes, seconds
# to display only part of the date
# all these functions return integers

print('Today is ' + str(today.day))
print('Month : ' + str(today.month))
print('Year: ' + str(today.year))
print('Hour : ' + str(today.hour))
print('Minutes : ' + str(today.minute))
print('Seconds : ' + str(today.second))
