#!usr/bin/env python3
import datetime

# Perform calculations with dates and times using timedelta
# create some date objects
dt1 = datetime.datetime(2019, 1, 15, 10)
print(dt1)
dt2 = datetime.datetime(2019, 1, 20, 15)
print(dt2)

# dates and times can be compared
print('Is dt1 smaller than dt2:', dt1 < dt2)
print('Is dt1 bigger than dt2:', dt1 > dt2)

# Subtracting one date from another creates a timedelta
# timedeltas represent a period of time rather than a specific time
delta = dt2 - dt1
print('timedelta of dt2-dt1:', delta)
# timedeltas have components
print('timedelta days:', delta.days)
print('timedelta secs:', delta.seconds)

# timedeltas can be used to perform date math
now = datetime.datetime.now()
oneyear = datetime.timedelta(days=365)
oneweek = datetime.timedelta(weeks=1)

print("One year from now will be: ", now + oneyear)
print("One week from now will be: ", now + oneweek)
print("One week ago was: ", now - oneweek)

# CONSOLE OUTPUT:
# Tue, Tuesday, 2,  2
# Jun, June, 06
# 08, 08, 29, 11, AM
# Tue Jun  2 08:29:11 2020
# 08:29:11
# today is:  06/02/20
# today is:  Tuesday 02, June 2020
# today is:  06/02/20 08:29 AM
