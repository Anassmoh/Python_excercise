main_menu_list = ["[1] Cast", "[2] Inventory", "[3] Settings", "[4] Exit"]
roadside_net, beach_net, lake_net = [], [], []
all_nets = [roadside_net, beach_net, lake_net]



def magnet_fishing(beeps):
    while beeps > 0:
        print("Beep")
        beeps -= 1
    return


def check_input(option, list):
    if option == "lopeta":
        pass
    elif int(option) > len(list) or int(option) < 0:
        print("invalid input")
    return

def main_menu():
    print("\nMAIN MENU\n")
    for menu in main_menu_list:
        print(menu)
    main_menu_option = choose_option()
    check_input(main_menu_option, main_menu_list)
    if main_menu_option == "1" and "[4] Restart" not in main_menu_list:
        main_menu_list.insert(3, "[4] Restart")
        main_menu_list[4] = "[5] Exit"
    return main_menu_option

def cast_menu():
    list_cast_menu = ["[1] Roadside", "[2] Beach", "[3] Lake", "[4] Main menu", "[5] Exit"]
    print("\nSELECT A MAP\n")
    for map in list_cast_menu:
        print(map)
    map_option = choose_option()
    check_input(map_option, list_cast_menu)
    if map_option == "1":
        magnet_fishing(5)
        metal_item = input("BEEP BEEP BEEP\nYou found some metal litter in the roadside, name the item and press ENTER to collect it to the net: ")
        roadside_net.append(metal_item)
    elif map_option == "2":
        magnet_fishing(8)
        metal_item = input("BEEP BEEP BEEP\nYou found some metal litter in the sand, name the item and press ENTER to collect it to the net: ")
        beach_net.append(metal_item)
    elif map_option == "3":
        magnet_fishing(10)
        metal_item = input("BEEP BEEP BEEP\nYou found some metal litter underwater, name the item and press ENTER to collect it to the net: ")
        lake_net.append(metal_item)
    elif map_option == "4":
        main_menu()
    elif map_option == "5" or map_option == "lopeta":
        exit = quit()
        return exit

def inventory_menu():
    list_inventory_menu = ["[1] All the nets ", "[2] Roadside net", "[3] Beach net", "[4] Lake net", "[5] Main menu", "[6] Exit"]    
    print("\nSELECT A NET\n")
    for net in list_inventory_menu:
        print(net)
    inventory_selection = choose_option()
    check_input(inventory_selection, list_inventory_menu)
    if inventory_selection == "1":
        print("\nThis is all your catch today:\n")
        for item in roadside_net:
            print(item)
        for item in beach_net:
            print(item)
        for item in lake_net:
            print(item)    
    elif inventory_selection == "2":
        print("\nThis is your roadside catch today:\n")
        for item in roadside_net:
            print(item)
    elif inventory_selection == "3":
        print("\nThis is your beach catch today:\n")
        for item in beach_net:
            print(item)
    elif inventory_selection == "4":
        print("\nThis is your lake catch today:\n")
        for item in lake_net:
            print(item)
    elif inventory_selection == "5":
        main_menu()
    elif inventory_selection == "6" or inventory_selection == "lopeta":
        exit = quit()
        return exit

def setting_menu():
    list_Setting_menu = ["[1] Recycle all the nets", "[2] Recycle a net", "[3] Main menu", "[4] Exit"]
    print("\nSELECT AN OPTION\n")
    for setting in list_Setting_menu:
        print(setting)
    setting_selection = choose_option()
    check_input(setting_selection, list_Setting_menu)
    if setting_selection == "1":
        roadside_net.clear() 
        beach_net.clear()
        lake_net.clear()
        print("\nAll the metal has been recycled, Well done!")
    elif setting_selection == "2":
        list_clear_menu = ["[1] Roadside net", "[2] Beach net", "[3] Lake net", "[4] Main menu", "[5] Exit"]
        print("\nSELECT A NET\n")
        for net in list_clear_menu:
            print(net)
        clear_selection = choose_option()
        check_input(clear_selection, list_clear_menu)
        if clear_selection == "1":
            roadside_net.clear()
            print("The roadside net's metals have been recycled, Well done!")
        elif clear_selection == "2":
            beach_net.clear()
            print("The beach net's metals have been recycled, Well done!")
        elif clear_selection == "3":
            lake_net.clear()
            print("The lake net's metals have been recycled, Well done!")
        elif clear_selection == "4":
            main_menu()
        elif clear_selection == "5" or clear_selection == "lopeta":
            exit = quit()
    elif setting_selection == "3":
        main_menu()
    elif setting_selection == "4" or setting_selection == "lopeta":
        exit = quit()
        return exit

def choose_option():
    option = input("\nSelect an option or type 'lopeta' to exit: ")
    return option


def quit():
    exit = input("The nets will be recycled, press Enter to exit or any other key to resume: ")
    if exit != "":
        menu_option = main_menu()
    return exit
        

name = input("Enter your name: ")
age = int(input("Enter your age: "))


while age >= 12:
    print(f"\n{name}, {age} years old.\n\nHello {name}, welcome to MagNet!")
    while True:
        main_menu_option = main_menu()
        if main_menu_option == "1":
            map_option = cast_menu()
        elif main_menu_option == "2":
            exit = inventory_menu()
            if exit == "":
                break
        elif main_menu_option == "3":
            setting_selection = setting_menu()
        elif main_menu_option == "4":
            if "[4] Restart" in main_menu_list:
                    restart = input("The progress will be lost, press Enter to confirm or any other key to resume: ")
                    if restart == "":
                        roadside_net.clear() 
                        beach_net.clear()
                        lake_net.clear()
                        print("All the metal have been recycled, Goodbye!")
                        break
                    else:
                        main_menu_option = main_menu()
            else:
                exit = quit()
                if exit == "":
                    break
        elif main_menu_option == "5" or main_menu_option == "lopeta":
            exit = quit()
            if exit == "":
                break
    if main_menu_option == "4" and "[4] Restart" in main_menu_list:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
    else:
        break

else: 
    if 0 < age < 12:
        print("Your age doesn't meet the minimum required, the game will exit immediately!")
    else:    
        print("invalid input")