airports = {}
menu = "\nAirport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit"
while True:
    option = int(input(f"{menu}\nPlease choose an option (1-3): "))
    if option == 1:
        ICAO = input("Enter the ICAO code: ")
        name = input("Enter the airport name: ")
        airports[ICAO] = name
        print(f"Airport {name} with ICAO code {ICAO} has been added.")
    elif option == 2:
        ICAO = input("Enter the ICAO code: ")
        if ICAO in airports:
            print(f"The airport with ICAO code {ICAO} is {airports[ICAO]}.")
        else:
            print(f"No airport found with ICAO code {ICAO}.")
    elif option == 3:
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break
    