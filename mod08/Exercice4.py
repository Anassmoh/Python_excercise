airports = {}

def new_airport(code, name):
    airports[code] = name
    print("Airport " + name + " with ICAO code " + code + " has been added.")
    return airports

while True:
    option = int(input("\nAirport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit\nPlease choose an option (1-3): "))
    if option == 1:
        code = input("Enter the ICAO code: ")
        name = input("Enter the airport name: ")
        airports = new_airport(code, name)
    elif option == 2:
        code = input("Enter the ICAO code: ")
        if code in airports:
            print("The airport with ICAO code " + code + " is " + airports[code] + ".")
        else:
            print("No airport found with ICAO code " + code + ".")
    else:
        break
print("Thank you for using the Airport Data Management system. Goodbye!")