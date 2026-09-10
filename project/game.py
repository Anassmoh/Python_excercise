list_main_menu = ["[1] Cast", "[2] Inventory", "[3] Settings", "[4] Exit"]
roadside_net, beach_net, lake_net = ["apple"], ["ll"], ["trop"]
main_net = [roadside_net, beach_net, lake_net]

def valid_input(selection, list):
    if selection == "lopeta":
        pass
    elif int(selection) > len(list) or int(selection) < 0:
        print("invalid input")
    return

def main_menu():
    print("MAIN MENU")
    for menu in list_main_menu:
        print(menu)
    menu_selection = input("Select an option or type 'lopeta' to exit: ")
    valid_input(menu_selection, list_main_menu)
    if menu_selection == 1 and "[4] Restart" not in list_main_menu:
        list_main_menu.insert(3, "[4] Restart")
        list_main_menu[4] = "[5] Exit"
    return menu_selection

def cast_menu():
    list_cast_menu = ["[1] Roadside", "[2] Beach", "[3] Lake", "[4] Main menu", "[5] Exit"]
    print("SELECT A MAP")
    for map in list_cast_menu:
        print(map)
    map_selection = input("Select an option or type 'lopeta' to exit: ")
    valid_input(map_selection, list_cast_menu)
    return map_selection

def inventory_menu():
    list_inventory_menu = ["[1] Main net ", "[2] Roadside", "[3] Beach", "[4] Lake", "[5] Main menu", "[6] Exit"]    
    print("SELECT A NET")
    for net in list_inventory_menu:
        print(net)
    inventory_selection = input("Select an option or type 'lopeta' to exit: ")
    valid_input(inventory_selection, list_inventory_menu)
    if inventory_selection == "1":
        print(main_net)
    elif inventory_selection == "2":
        print(roadside_net)
    elif inventory_selection == "3":
        print(beach_net)
    elif inventory_selection == "4":
        print(lake_net)
    elif inventory_selection == "5":
        main_menu()
    elif inventory_selection == "6" or inventory_selection == "lopeta":
        exit = lopeta()
        return exit

def setting_menu():
    list_Setting_menu = ["[1] Recycle all the nets", "[2] Recycle a net", "[3] Main menu", "[4] Exit"]
    for setting in list_Setting_menu:
        print(setting)
    setting_selection = input("Select an option or type 'lopeta' to exit: ")
    valid_input(setting_selection, list_Setting_menu)
    if setting_selection == "1":
        roadside_net.clear() 
        beach_net.clear()
        lake_net.clear()
        print("All the metal have been recycled, Well done!")
    elif setting_selection == "2":
        list_clear_menu = ["[1] Roadside", "[2] Beach", "[3] Lake", "[4] Main menu", "[5] Exit"]
        print("SELECT A NET")
        for net in list_clear_menu:
            print(net)
        clear_selection = input("Select an option or type 'lopeta' to exit: ")
        valid_input(clear_selection, list_clear_menu)
        if clear_selection == "1":
            roadside_net.clear()
            print("The roadside net's metals have been recycled, Well done!")
        elif clear_selection == "2":
            beach_net.clear()
            print("The beach net's metals have been recycled, Well done!")
        elif clear_selection == "3":
            lake_net.clear()
            print("The lake net's metals have been recycled, Well done!")
        elif clear_selection == "5":
            main_menu()
        elif clear_selection == "6" or clear_selection == "lopeta":
            exit = lopeta()
    elif setting_selection == "3":
        main_menu()
    elif setting_selection == "4" or setting_selection == "lopeta":
        exit = lopeta()
        return exit

def lopeta():
    exit = input("The nets will be recycled, press Enter to exit or any other key to resume: ")
    if exit != "":
        menu_selection = main_menu()
    return exit
        

name = input("Enter your name: ")
age = int(input("Enter your age: "))


if age >= 12:
    print(f"{name}, {age} years old.\nHello {name}, welcome to LootBall")
    while True:
        menu_selection = main_menu()
        if menu_selection == "1":
            map_selection = cast_menu()
        elif menu_selection == "2":
            exit = inventory_menu()
            if exit == "":
                break
        elif menu_selection == "3":
            setting_selection = setting_menu()
        elif menu_selection == "4" or menu_selection == "lopeta":
            exit = lopeta()
            if exit == "":
                break

        
elif 0 < age < 12:
    print("Your age doesn't meet the minimum required, the game will exit immediately!")
else:
    print("invalid input")

