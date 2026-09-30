import json
import time
import random
from classes.items_classes.items import Items, RoadsideItems, BeachItems, LakeItems
from functions.loading import measuring, processing, manual_scrap, demagnefy
from functions.check_input import name_age
from functions.menu_select import display, choose_option, check_input, naming_item

main_menu_list = [" [1]► Play", " [2]► Inventory", " [3]► Recycle", " [4]► Exit"]
#TODO: check inout for naming the littter after catching
def main_menu():
    player(name, age, total_income)
    print("\n\t\t\t\t◈  MAIN MENU  ◈\n")
    display(main_menu_list)
    main_menu_option = choose_option()
    check_input(main_menu_option, main_menu_list)
    return main_menu_option

def play_menu():
    play_menu_list = (" [1]► Roadside", " [2]► Beach", " [3]► Lake", " [4]► Main menu", " [5]► Exit")
    while True:
        player(name, age, total_income)
        print("\n\t\t\t\t◈  LITTER ZONES  ◈\n")
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
    for i in range(random.randint(4,9)):
        print(f"\r  μV", end='')
        time.sleep(0.5)
        print(f"\r0 μV", end='')
        time.sleep(0.5)
    voltage = random.randint(1,150)
    for n in range(8):
        time.sleep(0.3)
        print(f"\r{voltage + random.randint(-2,2)} μV", end='')
    for n in range(8):
        print(f"\r      !", end='')
        time.sleep(0.1)
        print(f"\r{voltage} μV", end='')
        time.sleep(0.2)
    print(f"              ")
    magnetude = random.choice([True,False])
    if magnetude == True:
        weight = voltage * 1.5
        matter = "Iron"
        demagnefy()
        measuring()
        print(f"\r{weight:.1f}g                                  ", end='')
        name = naming_item(weight, matter)        
        litter = Items(name, voltage, weight, matter)
    else:
        weight = voltage * 0.02
        if 0 < voltage <= 100:
            weight = voltage * 1.32
            matter = random.choice(["aluminium", "brass", "copper"])
            manual_scrap()
            measuring()
            print(f"\r{weight:.1f}g               ", end='')
            name = naming_item(weight, matter)            
            litter = Items(name, voltage, weight, matter)
        else:               
            weight = voltage * 0.02             
            matter = random.choice(["silver", "gold"])
            manual_scrap()
            measuring()
            print(f"\r{weight:.1f}g                      ", end='')
            name = naming_item(weight, matter)
            litter = Items(name, voltage, weight, matter)    
    return litter

def add_restart():
    if " [4]► Restart" not in main_menu_list:
        main_menu_list.insert(3, " [4]► Restart")
        main_menu_list[4] = " [5]► Exit"
    return main_menu_list

def inventory_menu():
    inventory_menu_list = (" [1]► All the nets ", " [2]► Roadside net", " [3]► Beach net", " [4]► Lake net", " [5]► Main menu", " [6]► Exit")
    player(name, age, total_income)
    print("\n\t\t\t\t◈  INVENTORY  ◈\n")
    display(inventory_menu_list)
    inventory_option = choose_option()
    check_input(inventory_option, inventory_menu_list)
    if inventory_option == "1" :
        if Items.all_count <= 1:
            print(f"\nYou collected {Items.all_count} item in total:")
        else:
            print(f"\nYou collected {Items.all_count} items in total:")
        if roadside_net.items_count == 0:
            print("\n➢ Roadside net is Empty.")
        else:
            print(end =''"\n➢ Roadside net")
            roadside_net.view_inventory()              
        if beach_net.items_count == 0:
            print("\n➢ Beach net is Empty")
        else:
            print(end =''"\n➢ Beach net")
            beach_net.view_inventory()
        if lake_net.items_count == 0:
            print("\n➢ Lake net is Empty")
        else:
            print(end =''"\n➢ Lake net")
            lake_net.view_inventory()
    elif inventory_option == "2":
        if roadside_net.items_count == 0:
            print("\n➢ Roadside net is empty.")
        else:
            print(end=''"\n➢ Roadside net ")
            roadside_net.view_inventory()
    elif inventory_option == "3":
        if beach_net.items_count == 0:
            print("➢ Beach net is empty.")
        else:
            print(end=''"\n➢ Beach net ")
            beach_net.view_inventory()
    elif inventory_option == "4":
        if lake_net.items_count == 0:
            print("➢ Lake net is empty.")
        else:
            print(end=''"\n➢ Lake net:")
            lake_net.view_inventory()
    elif inventory_option == "5":
        pass
    elif inventory_option == "6" or inventory_option == "lopeta":
        game_over = quit()
        return game_over

def sell(zone):
    price = zone.aluminium_price + zone.brass_price + zone.copper_price + zone.iron_price + zone.silver_price + zone.gold_price
    Items.all_count -= zone.items_count
    zone.items.clear()
    zone.items_count = 0
    zone.aluminium_weight = 0
    zone.aluminium_price = 0
    zone.brass_weight = 0
    zone.brass_price  = 0
    zone.copper_weight = 0
    zone.copper_price  = 0
    zone.iron_weight = 0
    zone.iron_price = 0
    zone.silver_weight = 0
    zone.silver_price = 0
    zone.gold_weight = 0
    zone.gold_price = 0
    return price

def recycle_menu():
    setting_menu_list = (" [1]► Recycle all", " [2]► Recycle a net", " [3]► Main menu", " [4]► Exit")
    player(name, age, total_income)
    print("\n\t\t\t\t◈  RECYCLING CENTER  ◈\n")
    display(setting_menu_list)
    setting_option = choose_option()
    check_input(setting_option, setting_menu_list)
    game_over = False # must set both values and return outside of loop to avoid error upon function call
    total = 0   
    if setting_option == "1" and Items.all_count != 0:
        roadside_income = sell(roadside_net)
        beach_income = sell(beach_net)
        lake_income = sell(lake_net)
        total = roadside_income + beach_income + lake_income
        processing()
        if total >= 1:
            print(f"\rWell done! You've made {total:.1f} Markkaa.")
        else:
            print(f"\rThe worth need to be at least 1 Markka.")
        time.sleep(2)
    elif setting_option == "2":
        recycle_menu_list = (" [1]► Recycle roadside net", " [2]► Recycle beach net", " [3]► Recycle lake net", " [4]► Main menu", " [5]► Exit")
        player(name, age, total_income)
        print("\n\t\t\t\t◈  RECYCLING CENTER  ◈\n")
        display(recycle_menu_list)
        recycle_option = choose_option()
        check_input(recycle_option, recycle_menu_list)
        if recycle_option == "1" and roadside_net.items_count != 0:
            roadside_income = sell(roadside_net)
            processing()
            if roadside_income >= 1:
                print(f"\rWell done! You've made {roadside_income:.1f} Markkaa.")
                total = roadside_income
            else:
                print(f"\rThe worth need to be at least 1 Markka.")
            time.sleep(2)
        elif recycle_option == "2" and beach_net.items_count != 0:
            beach_income = sell(beach_net)
            processing()
            if beach_income >= 1:
                print(f"\rWell done! You've made {beach_income:.1f} Markkaa.")
                total = beach_income
            else:
                print(f"\rThe worth need to be at least 1 Markka.")
            time.sleep(2)
        elif recycle_option == "3" and lake_net.items_count != 0:
            lake_income = sell(lake_net)
            processing()
            if lake_income >= 1:
                print(f"\rWell done! You've made {lake_income:.1f} Markkaa.")
                total = lake_income
            else:
                print(f"\rThe worth need to be at least 1 Markka.")
            time.sleep(2)
        elif recycle_option == "4":
            pass
        elif recycle_option == "5" or recycle_option == "lopeta":
            game_over = quit()
        else:
            print("\nThere is nothing to recycle in this net.")
    elif setting_option== "3":
        pass
    elif setting_option == "4" or setting_option == "lopeta":
        game_over = quit() #return has to be outside of loop 
    else:
        print("\nThere is no items to recycle.")
    return game_over, total

def restart_game():
    restart = input('The progress will be lost, are you sure you want to restart?\nType "yes" to confirm or any other key to resume: ')
    if restart.lower() == "yes":
        #TODO:clear the things decide how
        print("All the metal have been recycled, Goodbye!")
        restart = True
    else:
        restart = False
    return restart

def quit():
    game_over = input('Never quit before recycling, else you will not receive an income upon an automatic recycle\nType "yes" to confirm or any other key to resume: ')
    game_over = game_over.lower()
    if game_over == "yes":
        print("Goodbye!")
        time.sleep(1)
        game_over = True
        with open("save_checkpoint.txt", "w") as file:
            json.dump(players, file)
    else:
        game_over = False
    return game_over

def player(name, age, total_income):  # Displays those parametres on the top in every menu.
    print(f"\n\tPlayer: {name}  ★  Age: {age} yo  ★  Wallet: {total_income:.1f} Markkaa  ★  {2500-total_income:.1f} to target" )
    return

name, age = name_age()
total_income = 0 # must set to 0 to display wallet before reaching the IF that calls recycle function.
players = {}
with open("save_checkpoint.txt", "w") as file:
    json.dump(players, file)
with open("save_checkpoint.txt", "r") as file:
    players = json.load(file)
roadside_net = RoadsideItems()
beach_net = BeachItems()
lake_net = LakeItems()


while int(age) >= 12:
    restart = False # both has to be here in case loaded name doesn't match age, it will restart
    game_over = False
    if name in players and players[name][0] == int(age):
        total_income = players[name][1]
        print(f"\nHello {name}, welcome back to MagNet!")
    elif name in players and players[name][0] != age:
        print("Username already takken, try again")
        restart = True
        game_over = True
    else:
        print(f"\nHello {name}, welcome to MagNet!")
    while not game_over:
        main_menu_option = main_menu()
        if main_menu_option == "1":
            game_over = play_menu()
        elif main_menu_option == "2":
            game_over = inventory_menu()
        elif main_menu_option == "3":
            game_over, total = recycle_menu()
            total_income += total  # Adds money to wallet everytime you recycle
            if 0 < total_income < 2500:
                players[name] = [int(age), total_income]
            else:
                won = "Congratulations, you won the game!"
                print("\n\t\t\t\t", end='')
                for i in range(34):
                    print(f"{won[i]}", end='', flush = True)
                    time.sleep(0.08)
                players.pop(name)
                with open("save_checkpoint.txt", "w") as file:
                    json.dump(players, file)
                time.sleep(2)
                print("\n\t\t\t\t    The game will close now.\n")
                game_over = True
                time.sleep(2)
        elif main_menu_option == "4":
            if " [4]► Restart" in main_menu_list:
                restart = restart_game()
                if restart == True:
                    game_over = True
            else:
                game_over = quit() 
        elif (main_menu_option == "5" and " [4]► Restart" in main_menu_list) or main_menu_option == "lopeta":
            game_over = quit()
    if restart == True:
        main_menu_list = [" [1]► Play", " [2]► Inventory", " [3]► Recycle", " [4]► Exit"]
        name, age = name_age()
    elif game_over == True:
        break

else: 
    if int(age) < 12:
        print("Your age doesn't meet the minimum required, the game will exit immediately!")