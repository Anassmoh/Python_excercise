inch = float(input("Enter length in inches (negative value to quit): "))

while inch >= 0:
    cm = inch * 2.54
    print(f"{inch:.1f} inches is {cm:.2f} centimeters")
    inch = float(input("Enter length in inches (negative value to quit): "))
else:
    print("Program ended.")