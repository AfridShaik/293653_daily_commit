year = int(input("Please Enter a year: "))
if (year % 400 == 0):
    leap = True
elif (year % 100 == 0):
    leap = False
elif (year % 4 == 0):
    leap =True
else:
    leap = False
month = int(input("Enter a month between[1 to 12]: "))
if month in (1, 3, 5, 7, 8, 10, 12):
     pro = 31
elif month == 2:
    if leap:
        pro = 29
    else:
        pro = 28
else:
        pro = 30
day = int(input("Enter a day [1 to 31]: "))
if day < pro:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [dd-mm-yyyy] %d/%d/%d." % (day, month, year))