number = input("Enter a number (or press Enter to quit): ")
smallest, largest = float(number), float(number)
while number != "":
    if float(number) >= largest:
        largest = float(number)
    elif float(number) <= smallest:
        smallest = float(number)
    number = input("Enter a number (or press Enter to quit): ")

print(f"Smallest number: {smallest}\nLargest number: {largest}")