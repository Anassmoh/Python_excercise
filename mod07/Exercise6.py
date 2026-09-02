import math
def calculate_unit_price(diameter, price):
    value = price / ((diameter / 200) ** 2 * math.pi)
    return value
    

diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
price1 = float(input("Enter the price of the first pizza (euros): "))
diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
price2 = float(input("Enter the price of the second pizza (euros): "))

value1 = calculate_unit_price(diameter1, price1)
value2 = calculate_unit_price(diameter2, price2)

print(f"Unit price of the first pizza: {value1:.2f} euros/m²")
print(f"Unit price of the second pizza: {value2:.2f} euros/m²")

if value1 < value2:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")