from datetime import date, datetime
from datetime import timedelta
import datetime

print("date input format => dd/mm/yyyy")
format = "%d-%m-%Y"

dateToday = input("enter date of first revision : ")

rev0 = datetime.datetime.strptime(dateToday,format) # today
rev1 = rev0 + timedelta(days=1) # the next day
rev2 = rev1 + timedelta(days=3) # three days later
rev3 = rev2 + timedelta(days=7) # a week later
rev4 = rev3 + timedelta(days=30) # a month later

rev1 = datetime.datetime.strftime(rev1,format)
rev2 = datetime.datetime.strftime(rev2,format)
rev3 = datetime.datetime.strftime(rev3,format)
rev4 = datetime.datetime.strftime(rev4,format)

print("A day later : ",rev1)
print("Three days later : ",rev2)
print("A week later : ",rev3)
print("A month later :",rev4)