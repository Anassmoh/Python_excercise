#ask the user to select an option
menu_list = "select option: \n1. add \n2. substract \n3. multiply \n0. exit\n"
selection = input(menu_list)

#if user did not select quit

while selection != "0":
    #ask user for 2 numbers
    first_number = float(input("first number: "))
    second_number = float(input("second number: "))

    #perform selected calculation
    if selection == "1":
        print(f"result: {first_number + second_number}")
    elif selection == "2":
        print(f"result: {first_number - second_number}")
    elif selection == "3":
            print(f"result: {first_number * second_number}")
    else:
         print(f"incorrect option")
    menu_list = "select option: \n1. add \n2. substract \n3. multiply \n0. exit\n"
    selection = input(menu_list) 