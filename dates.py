import datetime
currentDate= (datetime.date.today()) # prints today date 2016-04-01

print currentDate.month
print currentDate.year
print currentDate.day

print currentDate.strftime('%d %b,%Y')

print currentDate.strftime('%d %b,%y')

"""
Please attend our event %A, %B %d in the year %Y
"""

print currentDate.strftime(('Please attend our event %A, %B %d in the year %Y'))
