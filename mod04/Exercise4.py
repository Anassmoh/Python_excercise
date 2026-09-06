year = int(input("Enter a year: "))
by_4 = year % 4
by_100 = year % 100
by_400 = year % 400

if by_400 == 0:
    print(year, "is a leap year.")
elif by_4 == 0 and by_100 != 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")