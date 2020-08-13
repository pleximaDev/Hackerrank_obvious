import calendar
import datetime

# month, day, year = raw_input().split()
month, day, year = (int(x) for x in raw_input().split())
# print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())

# datetime(year, day, month).weekday()
# datetime.datetime.today().weekday()

# ans = datetime.date(year, month, day)
# print (ans.strftime("%A"))
