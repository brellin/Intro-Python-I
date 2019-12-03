"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

current = str(datetime.date(datetime.utcnow()))
calendar.setfirstweekday(6)


def printCalendar():

    yyyymm = input('YYYY-MM: ')

    if (len(yyyymm) == 0):
        yyyymm = current

    lis = yyyymm.split('-')

    if (len(lis) == 1):

        if (len(lis[0]) == 4):
            lis.append(current.split('-')[1])

        elif (len(lis[0]) == (1 or 2)):
            lis.insert(0, current.split('-')[0])

        else:
            lis = current.split('-')

    year = int(lis[0])
    month = int(lis[1])

    print(calendar.month(year, month))


printCalendar()
