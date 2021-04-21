import calendar
from os import system

print("1. Total year calendar\n2. Specific Month calender")
try:
    option = int(input())
except:
    print("Wrong Choice")

if option != 1:
    try:
        year = int(input("Enter Year : "))
        month = int(input("Enter Month : "))
        system("clear")
        print(calendar.month(year,month))
    except  Exception as e:
        print("Input Number only!!!!!!!")
else:
    try:
        year = int(input("Enter Year : "))
        system("clear")
        print(calendar.calendar(year))
    except Exception as e:
        print("Input Number only!!!!!!!")

