#!usr/bin/env python3
from datetime import date, time, datetime

# create a new date object
d1 = date.today()
print('Today:', d1)
# access various components of the date object
print("Today's day:", d1.day)
print("Today's month:", d1.month)
print("Today's year:", d1.year)

# create a new time object
t1 = time(12, 30, 00)
print("Time:", t1)
# access various components of the time object
print("Time's hour:", t1.hour)

# create a new datetime object
dt1 = datetime.now()
print("Now:", dt1)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print("Now's month:", dt1.month)
print("Now's weekday:", dt1.weekday())
print("Now's weekday from given list:", days[dt1.weekday()])

# To modify values of date and time objects, use the replace function.
# These properties are read-only, if trying to modify them directly, we'll get
# an error.
d1 = d1.replace(year=2020, month=10, day=31)
t1 = t1.replace(hour=5)
dt1 = dt1.replace(year=2017, month=12)
print("Replaced date:", d1)
print("Replaced time:", t1)
print("Replaced datetime:", dt1)

# CONSOLE OUTPUT:
# Today: 2020-06-02
# Today's day: 2
# Today's month: 6
# Today's year: 2020
# Time: 12:30:00
# Time's hour: 12
# Now: 2020-06-02 08:06:41.637843
# Now's month: 6
# Now's weekday: 1
# Now's weekday from given list: Tue
# Replaced date: 2020-10-31
# Replaced time: 05:30:00
# Replaced datetime: 2017-12-02 08:06:41.637843
