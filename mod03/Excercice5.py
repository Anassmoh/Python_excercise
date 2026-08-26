talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_grams = 13.3 * (lots + pounds * 32 + talents * 20 * 32)

kilograms = int(total_grams / 1000)
remaining_grams = total_grams - (kilograms * 1000)
print(f"The weight in modern units: \n{kilograms} kilograms and {remaining_grams:.2f} grams.")