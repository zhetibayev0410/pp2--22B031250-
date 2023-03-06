#Write a Python program to subtract five days from current date.
import datetime
current_date = datetime.date.today()
five_days_ago = current_date - datetime.timedelta(days=5)
print("Five days ago was:", five_days_ago)


#Write a Python program to print yesterday, today, tomorrow.
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print("Yesterday was:", yesterday)
print("Today is:", today)
print("Tomorrow will be:", tomorrow)


#Write a Python program to drop microseconds from datetime.
import datetime

now = datetime.datetime.now()
now_without_microseconds = now.replace(microsecond=0)
print("Current date and time with microseconds:", now)
print("Current date and time without microseconds:", now_without_microseconds)


#Write a Python program to calculate two date difference in seconds
import datetime
date1 = datetime.datetime(2023, 3, 1, 0, 0, 0)
date2 = datetime.datetime(2023, 3, 6, 0, 0, 0)
difference = (date2 - date1).total_seconds()
print("The difference between the two dates in seconds is:", difference)
