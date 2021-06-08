import datetime
from datetime import date
from datetime import time
# from datetime import datetime
from datetime import timedelta

"""
    Print current date and time
"""

print(datetime.datetime.now())
print(datetime.datetime.now().date())
print(datetime.date.today())
print(datetime.datetime.now().time())

"""
    Print current day, month, year, time
"""

print(date.today().day)
print(date.today().month)
print(date.today().year)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)

"""
    Print given date
"""

print(datetime.date(2020, 12, 12))
print(datetime.datetime(2020, 12, 12, 22, 12, 12))
print(date.fromtimestamp(1326244364))
print(time(22, 10, 15, 423432))     # hour, minute, second and microseconds

"""
    Difference between two datetime
"""

d1 = datetime.datetime(year=date.today().year, month=date.today().month, day=date.today().day,
                       hour=datetime.datetime.now().hour, minute=datetime.datetime.now().minute,
                       second=datetime.datetime.now().second)
d2 = datetime.datetime(year=2021, month=1, day=1, hour=23, minute=0, second=0)
print(d1-d2)
d3 = date(2020, 1, 1)
d4 = date(2020, 12, 31)
print(d4-d3)


"""
    timedelta
"""
t = timedelta(days=4, hours=12, minutes=10)
print("Total seconds--->", t.total_seconds())
t1 = timedelta(weeks=2, days=2, hours=12, minutes=12, seconds=20)
t2 = timedelta(days=5, hours=12)
print("Timedelta difference--->", t1-t2)


"""
    Python format datetime
"""
current_datetime = datetime.datetime.now()
t = current_datetime.strftime('%H:%M:%S')
print('Current time->', t)

today_date = current_datetime.strftime('%d-%m-%Y %H:%M:%S')
print("today_date->", today_date)


"""
    strptime()-> String to datetime
"""
string_date_1 = "8 June 2021"
date_conversion_1 = datetime.datetime.strptime(string_date_1, '%d %B %Y')
print("date_conversion_1->", date_conversion_1)

string_date_2 = "2021-12-01 12:32:20"
date_conversion_2 = datetime.datetime.strptime(string_date_2, '%Y-%m-%d %H:%M:%S')
print("date_conversion_2->", date_conversion_2)

string_date_3 = "8 Jul 2021"
date_conversion_3 = datetime.datetime.strptime(string_date_3, '%d %b %Y')
print("date_conversion_3->", date_conversion_3)


"""
    Timezone operations
"""
import pytz
local = datetime.datetime.now()
print("Local time->", local)

tz_ny = pytz.timezone('America/New_York')
datetime_ny = datetime.datetime.now(tz_ny)
print("New York state time->", datetime_ny)
