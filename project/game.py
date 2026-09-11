import random
main_menu_list = ["[1] Cast", "[2] Inventory", "[3] Settings", "[4] Exit"]
roadside_net, beach_net, lake_net = [], [], []
all_nets = [roadside_net, beach_net, lake_net]

def add_restart():
    if "[4] Restart" not in main_menu_list:
        main_menu_list.insert(3, "[4] Restart")
        main_menu_list[4] = "[5] Exit"
    return main_menu_list

def restart_game():
    restart = input('The progress will be lost, are you sure you want to restart?\nType "yes" to confirm or any other key to resume: ')
    if restart.lower() == "yes":
        roadside_net.clear() 
        beach_net.clear()
        lake_net.clear()
        print("All the metal have been recycled, Goodbye!")
        main_menu_list = ["[1] Cast", "[2] Inventory", "[3] Settings", "[4] Exit"]
    else:
        pass
    return restart

def magnet_fishing():
    for _ in range(random.randint(3,8)):
        print("\nbeep..")
    return


def check_input(option, list):
    if option == "lopeta" or option == "":
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
    return main_menu_option

def cast_menu():
    list_cast_menu = ["[1] Roadside", "[2] Beach", "[3] Lake", "[4] Main menu", "[5] Exit"]
    print("\nSELECT A MAP\n")
    for map in list_cast_menu:
        print(map)
    map_option = choose_option()
    check_input(map_option, list_cast_menu)
    if map_option == "1":
        while True:
            magnet_fishing()
            metal_item = input("\nBEEP BEEP BEEP\nYou found some metal litter in the roadside, name the item and press ENTER to collect it to the net: ")
            roadside_net.append(metal_item)
            cast_again = input("Item added to the net!\nPress ENTER to cast your magnet or type any other key to change the map: ")
            if cast_again != "":
                cast_menu()
                main_menu_list = add_restart()
                break
        
    elif map_option == "2":
        while True:
            magnet_fishing()
            metal_item = input("\nBEEP BEEP BEEP\nYou found some metal litter in the sand, name the item and press ENTER to collect it to the net: ")
            beach_net.append(metal_item)
            cast_again = input("Item added to the net!\nPress ENTER to cast your magnet or type any other key to change the map: ")
            if cast_again != "":
                cast_menu()
                main_menu_list = add_restart()
                break
    elif map_option == "3":
        while True:
            magnet_fishing()
            metal_item = input("\nBEEP BEEP BEEP\nYou found some metal litter underwater, name the item and press ENTER to collect it to the net: ")
            lake_net.append(metal_item)
            cast_again = input("Item added to the net!\nPress ENTER to cast your magnet or type any other key to change the map: ")
            if cast_again != "":
                cast_menu()
                main_menu_list = add_restart()
                break
    elif map_option == "4":
        pass
    elif map_option == "5" or map_option == "lopeta":
        exit = quit()
        return exit

def inventory_menu():
    inventory_menu_list = ["[1] All the nets ", "[2] Roadside net", "[3] Beach net", "[4] Lake net", "[5] Main menu", "[6] Exit"]    
    print("\nSELECT A NET\n")
    for net in inventory_menu_list:
        print(net)
    inventory_option = choose_option()
    check_input(inventory_option, inventory_menu_list)
    if inventory_option == "1" :
        print("\nThis is all your catch so far:\n")
        if len(roadside_net) == 0:
            print("Roadside net : Empty")
        else:
            for item in roadside_net:
                print(item)
        if len(beach_net) == 0:
            print("Beach net : Empty")
        else:
            for item in beach_net:
                print(item)
        if len(lake_net) == 0:
            print("Lake net : Empty")
        else:
            for item in lake_net:
                print(item)    
    elif inventory_option == "2":
        if len(roadside_net) == 0:
            print("Your roadside net is empty")
        else:
            print("\nThis is your roadside catch so far:\n")
            for item in roadside_net:
                print(item)
    elif inventory_option == "3":
        if len(beach_net) == 0:
            print("Your beach net is empty")
        else:
            print("\nThis is your beach catch so far:\n")
            for item in beach_net:
                print(item)
    elif inventory_option == "4":
        if len(lake_net) == 0:
            print("Your lake net is empty")
        else:
            print("\nThis is your lake catch so far:\n")
            for item in lake_net:
                print(item)
    elif inventory_option == "5":
        pass
    elif inventory_option == "6" or inventory_option == "lopeta":
        exit = quit()
        return exit

def setting_menu():
    setting_menu_list = ["[1] Recycle all the nets", "[2] Recycle a net", "[3] Main menu", "[4] Exit"]
    print("\nSELECT AN OPTION\n")
    for setting in setting_menu_list:
        print(setting)
    setting_option = choose_option()
    check_input(setting_option, setting_menu_list)
    if setting_option == "1":
        roadside_net.clear() 
        beach_net.clear()
        lake_net.clear()
        print("\nAll the metal has been recycled, Well done!")
    elif setting_option == "2":
        clear_menu_list = ["[1] Roadside net", "[2] Beach net", "[3] Lake net", "[4] Main menu", "[5] Exit"]
        print("\nSELECT A NET\n")
        for net in clear_menu_list:
            print(net)
        clear_option = choose_option()
        check_input(clear_option, clear_menu_list)
        if clear_option == "1":
            roadside_net.clear()
            print("The roadside net's metals have been recycled, Well done!")
        elif clear_option == "2":
            beach_net.clear()
            print("The beach net's metals have been recycled, Well done!")
        elif clear_option == "3":
            lake_net.clear()
            print("The lake net's metals have been recycled, Well done!")
        elif clear_option == "4":
            main_menu_option = main_menu()
        elif clear_option == "5" or clear_option == "lopeta":
            exit = quit()
    elif setting_option== "3":
        pass
    elif setting_option == "4" or setting_option == "lopeta":
        exit = quit()
        return exit

def choose_option():
    option = input("\nSelect an option or type 'lopeta' to exit: ")
    return option


def quit():
    exit = input('Are you sure you want to quit?\nType "yes" to confirm or any other key to resume: ')
    exit = exit.lower()
    if exit == "yes":
        print("All the metal have been recycled, Goodbye!")
    else:
        pass
    return exit
        
def name_age():
    name = input("Enter your name: ")
    while name == "":
        print("invalid input")
        name = input("Enter your name: ")
        if name != "":
            break
    age = input("Enter your age: ")
    while age == "" or int(age) < 0:
        print("invalid input")
        age = input("Enter your age: ")
        if age != "":
            break
    name = name[0].upper() + name[1:].lower()
    return name, age

name, age = name_age()

while int(age) >= 12:
    print(f"\n{name}, {age} years old.\n\nHello {name}, welcome to MagNet!")
    while True:
        main_menu_option = main_menu()
        if main_menu_option == "1":
            exit = cast_menu()
            if exit == "yes":
                break
        elif main_menu_option == "2":
            exit = inventory_menu()
            if exit == "yes":
                break
        elif main_menu_option == "3":
            exit = setting_menu()
            if exit == "yes":
                break
        elif main_menu_option == "4":
            if "[4] Restart" in main_menu_list:
                restart = restart_game()
                if restart == "yes":
                    break
            else:
                exit = quit()
                if exit == "yes":
                    break
        elif main_menu_option == "5" or main_menu_option == "lopeta":
            exit = quit()
            if exit == "yes":
                break
    if exit == "yes":
        break
    elif restart == "yes":
        name, age = name_age()
        
else: 
    if int(age) < 12:
        print("Your age doesn't meet the minimum required, the game will exit immediately!")