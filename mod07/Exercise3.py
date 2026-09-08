def gallons_to_liters(gallons):
    litres = 3.785 * gallons
    return litres

while True:
    gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
    if gallons < 0:
        break
    print(f"{gallons} American gallons is {gallons_to_liters(gallons):.2f} liters.")
    
print("Program finished.")