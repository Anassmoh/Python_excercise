name = input("Enter your name: ")
age = int(input("Enter your age: "))


error = "Please select a valid option."

if age >= 12:
    print(f"{name}, {age} years old.\nHello {name}, welcome to LootBall")
    while True:
        print("Main menu \n[1] Start\n[2] Stats\n[3] settings\n[4] Lopeta")
        select = input("Select an option from 1 to 4, type 'lopeta' to exit: ")
        if select == "1":
            print("Starting game..")
        elif select == "2":
            print("progress not recorded")
        elif select == "3":
            select2 = input("[1] Change username \n[2] Email support \n[3] Back to main menu\nSelect an option for 1 to 3: ")
            if select2 == "1":
                name = input("Enter your name: ")
                print(F"{name}, {age} years old.")
            elif select2 == "2":
                print("support@lootball.com")
            elif select == "3":
                pass
            else:
                print(error)

        elif select == "4" or select == "lopeta":
            break
        else:
            print(error)
    
elif 0 < age < 12:
    print("Your age doesn't meet the minimum required, the game will exit immediately!")
else:
    print("invalid input")