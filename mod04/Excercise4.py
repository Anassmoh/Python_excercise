year = int(input("Enter a year: "))

test_1 = year % 4
test_2 = year % 100
test_3 = year % 400

if test_1 == 0 and test_2 != 0:
    print(str(year) + " is a leap year.")
elif test_3 == 0:
    print(str(year) + " is a leap year.")
else:
    print(str(year) + " is not a leap year.")

