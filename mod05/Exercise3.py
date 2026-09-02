number = input("Enter a number (or press Enter to quit): ")
biggest = number
smallest = number


if number == "":
    smallest = 0
    biggest = 0
    

while number != "":

    number = float(number)
    

    if float(biggest) < number:
         biggest = number
    elif float(smallest) > number:
         smallest = number
    elif float(smallest) == float(biggest) == number:
        
        smallest = float(smallest)
        biggest = float(biggest)
        smallest = float(biggest)
    
    
    number = input("Enter a number (or press Enter to quit): ")
else:
    print(f"Smallest number: {smallest:.1f} \nLargest number: {biggest:.1f}")


    
