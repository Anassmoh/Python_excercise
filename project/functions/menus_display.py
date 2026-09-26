from classes.items_classes import Items
from functions.active_magnet_fishing import magnet_fishing
from functions.input_check import check_input, choose_option
from shared import *



def display(menu_list):
    for menu in menu_list:
        print(menu)
    return

def main_menu():
    print("\nMAIN MENU\n")
    display(main_menu_list)
    main_menu_option = choose_option()
    check_input(main_menu_option, main_menu_list)
    return main_menu_option

def play_menu():
    play_menu_list = ("[1] Roadside", "[2] Beach", "[3] Lake", "[4] Main menu", "[5] Exit")
    while True:
        print("\nSELECT A MAP\n")
        display(play_menu_list)
        map_option = choose_option()
        check_input(map_option, play_menu_list)
        if map_option == "1":
            while True:
                cast = input("Press ENTER to cast your magnet or type any other key to change the map: ")
                if cast == "":
                    litter = magnet_fishing()
                    roadside_net.collectNprint(litter)
                else:
                    break
        elif map_option == "2":
            while True:
                cast = input("Press ENTER to cast your magnet or type any other key to change the map: ")
                if cast == "":
                    litter = magnet_fishing()
                    beach_net.collectNprint(litter)
                else:
                    break
        elif map_option == "3":
            while True:
                cast = input("Press ENTER to cast your magnet or type any other key to change the map: ")
                if cast == "":
                    litter = magnet_fishing()
                    lake_net.collectNprint(litter)
                else:
                    break
        elif map_option == "4":
            #TODO: this menu goes empty
            main_menu()
            break
            
        elif map_option == "5" or map_option == "lopeta":
            game_over = quit()
            return game_over

def inventory_menu():
    inventory_menu_list = ("[1] All the nets ", "[2] Roadside net", "[3] Beach net", "[4] Lake net", "[5] Main menu", "[6] Exit") 
    print("\nSELECT A NET\n")
    display(inventory_menu_list)
    inventory_option = choose_option()
    check_input(inventory_option, inventory_menu_list)
    if inventory_option == "1" :
        if Items.item_count <= 1:
            print(f"\nYou collected in total {Items.item_count} non-magnetic item and {roadside_net.total_weight + beach_net.total_weight + lake_net.total_weight }g of Iron:")
        else:
            print(f"\nYou collected in total {Items.item_count} non-magnetic items and {roadside_net.total_weight + beach_net.total_weight + lake_net.total_weight }g of Iron:")

        if len(roadside_net.items) == 0:
            print("\nRoadside net is Empty")
        else:
            print(end =''"\nRoadside net")
            roadside_net.view_inventory()
                
        if len(beach_net.items) == 0:
            print("\nBeach net is Empty")
        else:
            print(end =''"\nBeach net")
            beach_net.view_inventory()

        if len(lake_net.items) == 0:
            print("\nLake net is Empty")
        else:
            print(end =''"\nLake net")
            lake_net.view_inventory()

    elif inventory_option == "2":
        if len(roadside_net.items) == 0:
            print("\nYour roadside net is empty")
        else:
            print(end=''"\nRoadside net ")
            roadside_net.view_inventory()

    elif inventory_option == "3":
        if len(beach_net.items) == 0:
            print("Your beach net is empty")
        else:
            print(end=''"\nBeach net ")
            beach_net.view_inventory()
    elif inventory_option == "4":
        if len(lake_net.items) == 0:
            print("Your lake net is empty")
        else:
            print(end=''"\nLake net:")
            lake_net.view_inventory()
            
    elif inventory_option == "5":
        main_menu()
    elif inventory_option == "6" or inventory_option == "lopeta":
        game_over = quit()
        return game_over

def setting_menu():
    setting_menu_list = ("[1] Recycle all the nets", "[2] Recycle a net", "[3] Main menu", "[4] Exit")
    print("\nSELECT AN OPTION\n")
    display(setting_menu_list)
    setting_option = choose_option()
    check_input(setting_option, setting_menu_list)
    if setting_option == "1":
        roadside_net.clear() 
        beach_net.clear()
        lake_net.clear()
        print("\nAll the metal has been recycled, Well done!")
    elif setting_option == "2":
        recycle_menu_list = ("[1] Roadside net", "[2] Beach net", "[3] Lake net", "[4] Main menu", "[5] Exit")
        print("\nSELECT A NET\n")
        display(recycle_menu_list)
        recycle_option = choose_option()
        check_input(recycle_option, recycle_menu_list)
        if recycle_option == "1":
            roadside_net.clear()
            print("The roadside net's metals have been recycled, Well done!")
        elif recycle_option == "2":
            beach_net.clear()
            print("The beach net's metals have been recycled, Well done!")
        elif recycle_option == "3":
            lake_net.clear()
            print("The lake net's metals have been recycled, Well done!")
        elif recycle_option == "4":
            main_menu_option = main_menu()
        elif recycle_option == "5" or recycle_option == "lopeta":
            game_over = quit()
    elif setting_option== "3":
        pass
    elif setting_option == "4" or setting_option == "lopeta":
        game_over = quit()
    return game_over

