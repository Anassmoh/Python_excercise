import time
import random
from classes.items_classes.items import Items, RoadsideItems, BeachItems, LakeItems
from functions.check_input import name_age
from functions.menu_select import display, choose_option, check_input

main_menu_list = [" [1]► Play", " [2]► Inventory", " [3]► Recycle", " [4]► Exit"]

def main_menu():
    print("\n◈ MAIN MENU ◈\n")
    display(main_menu_list)
    main_menu_option = choose_option()
    check_input(main_menu_option, main_menu_list)
    return main_menu_option

def play_menu():
    play_menu_list = (" [1]► Roadside", " [2]► Beach", " [3]► Lake", " [4]► Main menu", " [5]► Exit")
    while True:
        print("\n◈ LITTER ZONES ◈\n")
        display(play_menu_list)
        map_option = choose_option()
        check_input(map_option, play_menu_list)
        if map_option == "1":
            while True:
                cast = input("Press ENTER to cast your magnet or type any other key to change the zone: ")
                if cast == "":
                    litter = magnet_fishing()
                    roadside_net.collectNprint(litter)
                else:
                    break
        elif map_option == "2":
            while True:
                cast = input("Press ENTER to cast your magnet or type any other key to change the zone: ")
                if cast == "":
                    litter = magnet_fishing()
                    beach_net.collectNprint(litter)
                else:
                    break
        elif map_option == "3":
            while True:
                cast = input("Press ENTER to cast your magnet or type any other key to change the zone: ")
                if cast == "":
                    litter = magnet_fishing()
                    lake_net.collectNprint(litter)
                else:
                    break
        elif map_option == "4":
            break
        elif map_option == "5" or map_option == "lopeta":
            game_over = quit()
            return game_over

def magnet_fishing():
            add_restart()
            for i in range(random.randint(4,12)):
                print(f"\r  μV", end='')
                time.sleep(0.5)
                print(f"\r0 μV", end='')
                time.sleep(0.5)
            voltage = random.randint(1,150)
            for n in range(8):
                time.sleep(0.3)
                print(f"\r{voltage + random.randint(-2,2)} μV", end='')
            magnetude = random.choice([True,False])
            if magnetude == True:
                weight = voltage * 1.5
                matter = "Iron"
                for n in range(8):
                    print(f"\r      !", end='')
                    time.sleep(0.2)
                    print(f"\r{voltage} μV", end='')
                    time.sleep(0.2)
                    
                name = input(f"\nYou found {weight}g of {matter}, name the item and press ENTER to collect it to the net: ")
                litter = Items(name, voltage, weight, matter)
            else:
                weight = "N/A"
                if 0 < voltage <= 50:
                    matter = random.choice(["aluminum", "brass"])
                    name = input(f"\nYou found some {matter}, name the item and press ENTER to collect it to the net: ")
                    litter = Items(name, voltage, weight, matter)
                elif 50 < voltage <= 100:
                    matter = random.choice(["silver", "copper"])
                    name = input(f"\nYou found some {matter}, name the item and press ENTER to collect it to the net: ")
                    litter = Items(name, voltage, weight, matter)
                else:                            
                    matter = "gold"
                    name = input(f"\nCongratulations! You found some {matter}, name the item and press ENTER to collect it to the net: ")
                    litter = Items(name, voltage, weight, matter)    
            return litter

def add_restart():
    if "[4]► Restart" not in main_menu_list:
        main_menu_list.insert(3, " [4]► Restart")
        main_menu_list[4] = " [5]► Exit"
    return main_menu_list

def inventory_menu():
    inventory_menu_list = (" [1]► All the nets ", " [2]► Roadside net", " [3]► Beach net", " [4]► Lake net", " [5]► Main menu", " [6]► Exit") 
    print("\n◈ INVENTORY ◈\n")
    display(inventory_menu_list)
    inventory_option = choose_option()
    check_input(inventory_option, inventory_menu_list)
    if inventory_option == "1" :
        if Items.item_count <= 1:
            print(f"\nYou collected in total {Items.item_count} non-magnetic item and {roadside_net.total_weight + beach_net.total_weight + lake_net.total_weight }g of Iron:")
        else:
            print(f"\nYou collected in total {Items.item_count} non-magnetic items and {roadside_net.total_weight + beach_net.total_weight + lake_net.total_weight }g of Iron:")
        if len(roadside_net.items) == 0:
            print("\n➢Roadside net is Empty")
        else:
            print(end =''"\n➢Roadside net")
            roadside_net.view_inventory()              
        if len(beach_net.items) == 0:
            print("\n➢Beach net is Empty")
        else:
            print(end =''"\n➢Beach net")
            beach_net.view_inventory()
        if len(lake_net.items) == 0:
            print("\n➢Lake net is Empty")
        else:
            print(end =''"\n➢Lake net")
            lake_net.view_inventory()
    elif inventory_option == "2":
        if len(roadside_net.items) == 0:
            print("\n➢Roadside net is empty")
        else:
            print(end=''"\n➢Roadside net ")
            roadside_net.view_inventory()
    elif inventory_option == "3":
        if len(beach_net.items) == 0:
            print("➢Beach net is empty")
        else:
            print(end=''"\n➢Beach net ")
            beach_net.view_inventory()
    elif inventory_option == "4":
        if len(lake_net.items) == 0:
            print("➢Lake net is empty")
        else:
            print(end=''"\n➢Lake net:")
            lake_net.view_inventory()
    elif inventory_option == "5":
        pass
    elif inventory_option == "6" or inventory_option == "lopeta":
        game_over = quit()
        return game_over

def recycle_menu():
    setting_menu_list = (" [1]► Recycle all", " [2]► Recycle a net", " [3]► Main menu", " [4]► Exit")
    print("\n◈ RECYCLING CENTER ◈\n")
    display(setting_menu_list)
    setting_option = choose_option()
    check_input(setting_option, setting_menu_list)
    if setting_option == "1":
        roadside_net.items.clear()
        beach_net.items.clear()
        lake_net.items.clear()
        Items.item_count = 0
        roadside_net.total_weight = 0
        beach_net.total_weight = 0
        lake_net.total_weight = 0
        print("\nAll the metal has been recycled, Well done!")
    elif setting_option == "2":
        recycle_menu_list = (" [1]► Recycle roadside net", " [2]► Recycle beach net", " [3]► Recycle lake net", " [4]► Main menu", " [5]► Exit")
        print("\n◈ RECYCLING CENTER ◈\n")
        display(recycle_menu_list)
        recycle_option = choose_option()
        check_input(recycle_option, recycle_menu_list)
        if recycle_option == "1":
            roadside_net.items.clear()
            Items.item_count -= roadside_net.non_magnetic_items
            roadside_net.non_magnetic_items = 0
            roadside_net.total_weight = 0
            print("The roadside net's metals have been recycled, Well done!")
        elif recycle_option == "2":
            beach_net.items.clear()
            Items.item_count -= beach_net.non_magnetic_items
            beach_net.non_magnetic_items = 0
            beach_net.total_weight = 0
            print("The beach net's metals have been recycled, Well done!")
        elif recycle_option == "3":
            lake_net.items.clear()
            Items.item_count -= lake_net.non_magnetic_items
            lake_net.non_magnetic_items = 0
            lake_net.total_weight = 0
            print("The lake net's metals have been recycled, Well done!")
        elif recycle_option == "4":
            pass
        elif recycle_option == "5" or recycle_option == "lopeta":
            game_over = quit()
    elif setting_option== "3":
        pass
    elif setting_option == "4" or setting_option == "lopeta":
        game_over = quit()
        return game_over

def restart_game():
    restart = input('The progress will be lost, are you sure you want to restart?\nType "yes" to confirm or any other key to resume: ')
    if restart.lower() == "yes":
        roadside_net.items.clear() 
        beach_net.items.clear()
        lake_net.items.clear()
        print("All the metal have been recycled, Goodbye!")
    return restart

def quit():
    game_over = input('Are you sure you want to quit?\nType "yes" to confirm or any other key to resume: ')
    game_over = game_over.lower()
    if game_over == "yes":
        print("All the metal have been recycled, Goodbye!")
        game_over = True
    else:
        game_over = False
    return game_over

name, age = name_age()
roadside_net = RoadsideItems()
beach_net = BeachItems()
lake_net = LakeItems()

while int(age) >= 12:
    print(f"\n{name}, {age} years old.\n\nHello {name}, welcome to MagNet!")
    game_over = False
    while not game_over:
        main_menu_option = main_menu()
        if main_menu_option == "1":
            game_over = play_menu()
        elif main_menu_option == "2":
            game_over = inventory_menu()
        elif main_menu_option == "3":
            game_over = recycle_menu()
        elif main_menu_option == "4":
            if "[4]► Restart" in main_menu_list:
                restart = restart_game()
                if restart == "yes":
                    break
            else:
                game_over = quit()
        elif (main_menu_option == "5" and " [4]► Restart" in main_menu_list) or main_menu_option == "lopeta":
            game_over = quit()
    if game_over == True:
        break        
    elif restart == "yes":
        main_menu_list = [" [1]► Play", " [2]► Inventory", " [3]► Settings", " [4]► Exit"]
        name, age = name_age()
else: 
    if int(age) < 12:
        print("Your age doesn't meet the minimum required, the game will exit immediately!")

