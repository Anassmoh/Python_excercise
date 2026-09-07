number = input("Enter a number (or press Enter to quit): ")
smallest = largest = number

while number != "":
    number = float(number)
    smallest = float(smallest)
    largest = float(largest)
    if number < smallest:
        smallest = number
    elif number > largest:
        largest = number
    number = input("Enter a number (or press Enter to quit): ")

if largest == "":
    print("Smallest number: 0.0 \nLargest number: 0.0")
# considering the first input is an empty string
else:
    print(f"Smallest number: {smallest:.1f} \nLargest number: {largest:.1f}")