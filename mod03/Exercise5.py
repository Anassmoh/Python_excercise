talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_grams = 13.3 * (talents * 20 * 32 + pounds * 32 + lots)
remaining_grams = total_grams % 1000
kilograms = (total_grams - remaining_grams) / 1000

print(f"The weight in modern units: \n{kilograms:.0f} kilograms and {remaining_grams:.2f} grams.")