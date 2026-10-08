import json
import time
import random
from classes.items import Items, RoadsideItems, BeachItems, LakeItems
from functions.loading import measuring, processing, manual_scrap, demagnify
from functions.check_input import name_age
from functions.menu_select import display, choose_option, check_input, naming_item
from functions.display_text import intro_print, instru_print

main_menu_list = [" [1]► Play", " [2]► Inventory", " [3]► Recycle", " [4]► Exit"]
battery = 100

# For testing purposes, you can:
# 1. Press ctrl + b to close the breakpoint and have a full code screen view.
# 2. Lower the "battery" value from 100 to 22 (line 11).
# 3. Higher the total_income from the save_checkpoint disctionnary to 2400, or...
#    Alternatively lower the target from 2500 to 100 markkaa (line 359 and 361).
# 4. You can also "comment" intro_print() (line 321) and instru_print() (line 348) by adding # 
#    to jump straight to the menu.

# The following functions have to reside in the main code, as they are heavily interconnected.
# Importing them from differents files will lead to an inevitable cirtcular import.

def main_menu():  # displays main menu and player info, allows you to choose an option, chekcs it and returns it.
    player(name, age, total_income)   # diplays player info on top of the menu
    print("\n\t\t\t\t◈  MAIN MENU  ◈\n")
    display(main_menu_list)   # displays the menu (for loop)
    main_menu_option = choose_option()  # return the option that you input
    check_input(main_menu_option, main_menu_list) # checks if the option is valid format and is in the range of the menu.
    return main_menu_option

def low_battery(): # Warns you if the battery is less than 15%.
    if battery < 15:
        print(f"\rYour battery is running low! {battery}%    ", end='')
        time.sleep(0.6)
        for i in range(3):
            print("\r                                 ", end='')
            time.sleep(0.5)
            print(f"\rYour battery is running low! {battery}%    ", end='')
            time.sleep(0.6)
    return

def zone_menu(): # displays litter zones menu and player info, allows you to choose an option, checks it and returns it.
    zone_menu_list = (" [1]► Roadside", " [2]► Beach", " [3]► Lake", " [4]► Main menu", " [5]► Exit")
    while battery > 0: # TODO: This loop works but maybe unnecessary condition, "while True" might work also.  
        player(name, age, total_income) # diplays player info on top of the menu
        print("\n\t\t\t\t◈  LITTER ZONES  ◈\n")
        display(zone_menu_list)  # displays the menu
        zone_option = choose_option()  # return the option that you input
        check_input(zone_option, zone_menu_list)  # checks if the option is valid format and is in the range of the menu.
        if zone_option == "1":
            while True: # keeps allowing you to play in the same zone.
                if battery == 0:
                    zone_option == "4" 
                    break  # breaks from while True loop and jumps to option 4 which is main menu instead of zone menu.
                low_battery() # displays a warning msg if battery is low.
                cast = input("\rPress ENTER to cast MagMed or type any other key to change the zone: ")
                if cast == "":
                    litter = magnet_fishing() # displays effects, chooses random(int, boolean, str), allows you to name your litter.
                    roadside_net.collectNprint(litter) #This method saves name, weight, matter and price in the RoadsideItem initializer.
                else:
                    break # Kicks you out back to litter zones menu to change the zone.
        elif zone_option == "2":
            while True:
                if battery == 0:
                    zone_option == "4"
                    break
                low_battery()
                cast = input("\rPress ENTER to cast MagMed or type any other key to change the zone: ")
                if cast == "":
                    litter = magnet_fishing()
                    beach_net.collectNprint(litter) # same method that saves the info, but in the super class initializer (RoadsideNet).
                else:
                    break
        elif zone_option == "3":
            while True:
                zone_option == "4"
                if battery == 0:
                    break
                low_battery()
                cast = input("\rPress ENTER to cast MagMed or type any other key to change the zone: ")
                if cast == "":
                    litter = magnet_fishing()
                    lake_net.collectNprint(litter) # same method that saves the info, but in the super class initializer (RoadsideNet).
                else:
                    break
        elif zone_option == "4":
            break
        elif zone_option == "5" or zone_option == "lopeta":
            game_over = quit() # Function starts the quiting process, prevents from accidental exit.
            return game_over # boolean value, returns False if quiting process was aborted.
        
        
def magnet_fishing(): 
    add_restart() # call : adds a restart option in the main menu once you cast your magnet.
    for i in range(random.randint(4,9)): # visuals that mimics a metal detector scanning.
    #TODO : +idea: add the static item count to random range (4+Item.All_count, 9+Item.All_count) 
        # to make it seem harder and more rare to find items the more you collect.
        print(f"\r  μV", end='')
        time.sleep(0.5)
        print(f"\r0 μV", end='')
        time.sleep(0.5)
    voltage = random.randint(1,150) # Gives a random voltage number that will determine the weight and the matter of the litter.
    for n in range(8):  # mimics a nearby item detection.
        time.sleep(0.3)
        print(f"\r{voltage + random.randint(-2,2)} μV", end='') 
    for n in range(8):    #  mimics a definite find.
        print(f"\r      ! ", end='')
        time.sleep(0.1)
        print(f"\r{voltage} μV", end='')
        time.sleep(0.2)
    print(f"              ")
    magnetude = random.choice([True,False])   # randomly determines the matter of the litter, "Iron" if True.
    if magnetude == True:
        weight = voltage * 1.5
        matter = "Iron"
        demagnify()        # tells you that you are collecting the litter from the magnet, a hint that you found iron.
        measuring()        # print visual msg, acting like you are measuring the litter weight.
        print(f"\r{weight:.1f}g                                  ", end='')
        name = naming_item(weight, matter)  # Prints  finding info, allows you to name it, else gives it a standard matter label.
        litter = Items(name, voltage, weight, matter) # Create an object, keeps track of your overall items, not zone specific.
    else:
        weight = voltage * 0.02
        if 0 < voltage <= 100:
            weight = voltage * 1.32
            matter = random.choice(["aluminium", "brass", "copper"])
            manual_scrap()   # tells you that you are manually collecting the item, a hint that it's other than iron.
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
    global battery # throws the next local value to the global variable. better than using "return" since functions are interconnected.
#TODO:+idea: learn about threading to run things simultaniously, battery drop can be done by time.time() and a time_stamp difference.
    battery -= random.randint(1,3)  #random battery drop after every magnet cast
    if battery < 0:    # restricts battery value to go negative.
        battery = 0
    return litter

#TODO: Restart initially was added to the menu only after casting the magnet, after introducing income, a player should be able
# to restart the game after continuing the game and loading his income back (restart not in menu despite income is more than 0)
# restart should be added based on income not items in net.  FIXED!
def add_restart():    # adds restart if not already in main menu, pushed exit to number 5.
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
        if Items.all_count <= 1: # this shared value by all instances would tell you if there is any item anywhere.
            print(f"\nYou collected {Items.all_count} item in total:")
        else:
            print(f"\nYou collected {Items.all_count} items in total:")
        if roadside_net.items_count == 0: # in assosiation with the previous one, but also has its own count.
            print("\n➢ Roadside net is Empty.")
        else:
            print(end =''"\n➢ Roadside net") # prints in the beginning same line of the very next print.
            roadside_net.view_inventory()   # prints zone specific item count and displays their name and weight.
        if beach_net.items_count == 0:
            print("\n➢ Beach net is Empty")
        else:
            print(end =''"\n➢ Beach net")
            beach_net.view_inventory() #prints zone specific item count and displays their name and weight (inheritance)
        if lake_net.items_count == 0:
            print("\n➢ Lake net is Empty")
        else:
            print(end =''"\n➢ Lake net")
            lake_net.view_inventory() #prints zone specific item count and displays their name and weight (inheritance)
    elif inventory_option == "2":  # same as option 1, but ignore the static count, and focuses on zone specific count and list content.
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
#zone specific: Calculate total and returns price of a collection, set all values to 0. and substract it from static count.
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

def recycle_menu(): #
    recycle_menu_list = (" [1]► Recycle all", " [2]► Recycle a net", " [3]► Main menu", " [4]► Exit")
    player(name, age, total_income)
    print("\n\t\t\t\t◈  RECYCLING CENTER  ◈\n")
    display(recycle_menu_list)
    recycle_option = choose_option()
    check_input(recycle_option, recycle_menu_list)
    game_over = False # +next ine : must set both values and return outside of loop to avoid return error upon function call.
    total = 0
    if recycle_option == "1" and Items.all_count != 0: # sells only if there is an item in any zone collection..
        roadside_income = sell(roadside_net) # +next 2 line : calculate total price of each zone, return it, then restet values to back to 0.
        beach_income = sell(beach_net)
        lake_income = sell(lake_net)
        total = roadside_income + beach_income + lake_income #combines all the zone income after a general recycle
        processing()  #visual : mimics recycle loading 0% to 100%
        if total >= 1: # ignores if total income is too small.
            print(f"\rWell done! You've made {total:.1f} Markkaa.")
        else:
            print(f"\rThe worth need to be at least 1 Markka.")
        time.sleep(2)
    elif recycle_option == "2": # displays a zone specific inventory
        recycle_menu_list = (" [1]► Recycle roadside net", " [2]► Recycle beach net", " [3]► Recycle lake net", " [4]► Main menu", " [5]► Exit")
        player(name, age, total_income)
        print("\n\t\t\t\t◈  RECYCLING CENTER  ◈\n")
        display(recycle_menu_list)
        recycle_option = choose_option()
        check_input(recycle_option, recycle_menu_list)
        if recycle_option == "1" and roadside_net.items_count != 0: # sells only if there is an item in the specific zone collection..
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
        elif 1 <= int(recycle_option) <= 3 and Items.all_count == 0:
            print("\nThere is nothing to recycle in this net.")
    elif recycle_option== "3":
        pass
    elif recycle_option == "4" or recycle_option == "lopeta":
        game_over = quit() #return has to be outside of loop 
    elif recycle_option == "1" and Items.all_count == 0:
        print("\nThere is no items to recycle.")
    return game_over, total # return placed outside loop since values are always attributed to both variables.

def restart_game(): #allows you to restart the game by removing the current player, and adding new one without kicking out of game.
    restart = input('Your progress will be reset, are you sure you want to restart?\nType "yes" to confirm or any other key to resume: ')
    if restart.lower() == "yes": #Prevents from accidental restart, ignore case sensitivity.
        #TODO: recheck if it works.
        print(f"Goodbye {name}!")
        if name in players: #only deletes if account has been already saved.
            players.pop(name) #removes the player from the dictionnary.
            with open("project/save_checkpoint.txt", "w") as file:  #saves the account modification.
                json.dump(players, file)
        restart = True
    else:
        restart = False
    return restart #Returns a boolean value, false if restarting process aborted.

def quit(): #Not only allows you to quit the game, but the only way to save your progress.
    game_over = input('Never quit before recycling, else you will not receive an income upon an automatic recycle\nType "yes" to confirm or any other key to resume: ')
    game_over = game_over.lower() #Prevents from accidental quiting, ignores case sensitivity.
    if game_over == "yes":
        if total_income > 0: #in case you had some income it will save your account
            print(f"Progress saved! see you soon {name}!")
            time.sleep(1)
            game_over = True
            with open("project/save_checkpoint.txt", "w") as file: #saves your progress.
                json.dump(players, file)
        else:  #with no income, the game can't be saved since the items will be recycled anyway.
            print(f"Goodbye {name}!")
            time.sleep(1)
            game_over = True
    else:
        game_over = False
    return game_over #Returns a boolean value, false if quiting process aborted.

def player(name, age, total_income):  # Displays those parametres on the top in every menu.
    print(f"\n\tPlayer: {name}  ★  Age: {age} yo  ★  Wallet: {total_income:.1f} Markkaa  ★  {battery}% battery")
    return

intro_print()

name, age = name_age() #Returns the name and age that you input.
total_income = 0 #Must be set to 0 to display wallet before reaching the recycle function that returns income.

players = {} #dictionnary that holds name, age and income. it is the variable that get saved after quiting the game.

with open("project/save_checkpoint.txt", "r") as file: #Import the "accounts" dictionary.
    players = json.load(file)

roadside_net = RoadsideItems() #Creates object in assosiation with the overall item class
beach_net = BeachItems() #+next line: Creates object in assosiation with the overall item class, by inheritance of previous superClass.
lake_net = LakeItems()

while int(age) >= 12:
    restart = False #+next line : both has to be here in case loaded name doesn't match age. 
    game_over = False
    if name in players and players[name][0] == int(age): #Checks if name and age already in dictionnary.
        total_income = players[name][1] # set the income to whatever you left it in the last checkpoint save.
        add_restart()
        print(f"\nHello {name}, welcome back to MagNet!")
    elif name in players and players[name][0] != age: #Prevents from overwriting age, in case name doesn't match age in the dictionnary.
        print("Username already takken, try again")
        restart = True # +next line: Allows you to keep tryng names till it's new player, or an account info matches in the dictionnary.
        game_over = True
    else:
        time.sleep(0.2)
        print(f"\nHello {name}, welcome to MagNet!")
        time.sleep(0.5)
        instru_print()
    while not game_over:
        while battery > 0: #as long as there is battery, game will not end 
            main_menu_option = main_menu() #First menu to be displayed after name and age checks out.
            if main_menu_option == "1":  #Options of the main menu.
                game_over = zone_menu()  #Options of the specific menu, all return True/False as you can exit game from every menu.
            elif main_menu_option == "2":  
                game_over = inventory_menu()
            elif main_menu_option == "3":
                game_over, total = recycle_menu()  #Returns also the total, to add it to the wallet.
                total_income += total  # Adds money to wallet everytime you recycle.
                if 0 < total_income < 2500: #Play as long as target is not reached (2500 markkaa)
                    players[name] = [int(age), total_income]
                elif total_income >= 2500: #Target reached, game will end and player will be deleted so he can play again.
                    won = "Congratulations, you won the game!"
                    print("\n\t\t\t\t", end='')
                    for i in range(34):  #visuals in the middle of the screen, forced to print in each iteration
                        print(f"{won[i]}", end='', flush=True)
                        time.sleep(0.08)
                    thanks = "Thank you for your daily contribution for a sustainable lifestyle."
                    time.sleep(1)
                    print("\n\t\t ", end='')
                    for i in range(66):  
                        print(f"{thanks[i]}", end='', flush=True)
                        time.sleep(0.08)                        
                    players.pop(name)   #Deletes player, so won't prevent him to play again (win error everytime he loads 2500 markkaa).
                    with open("project/save_checkpoint.txt", "w") as file:
                        json.dump(players, file)
                    time.sleep(1)
                    print("\n\t\t\t\t     Recycling your account...")
                    time.sleep(1)
                    print("\t\t\t\t\tSee you tomorrow!\n")
                    game_over = True   #Breaks loop
                    time.sleep(2)
            elif main_menu_option == "4": #Action depends on whether restart or quit is in index 3.
                if " [4]► Restart" in main_menu_list:
                    restart = restart_game()
                    if restart == True:
                        game_over = True
                else:
                    game_over = quit()
            elif (main_menu_option == "5" and " [4]► Restart" in main_menu_list) or main_menu_option == "lopeta":
                #3 conditions to start quiting process, not to mess with check_input function that check length of menu options.
                game_over = quit()
            if game_over == True:
                break
        else:
            print("Battery drained, charge your MagMed")
            time.sleep(3)
            game_over = True
            break
    if restart == True: #If restart process is definite, will turn main_menu back to normal.
        main_menu_list = [" [1]► Play", " [2]► Inventory", " [3]► Recycle", " [4]► Exit"]
        intro_print()
        name, age = name_age()
        total_income = 0 #+next: reset both values, else new player will carry on the deleted player's progress
        battery = 100
    elif game_over == True:
        break

else: 
    if int(age) < 12:
        print("Your age doesn't meet the minimum required, the game will exit immediately!")

#TODO : +idea: allow the player to utilize his income to charge his battery, the target then can be highered...
#        New specifications can be also available to buy for MagMed such as more powerful voltage emission, a 
#        stronger magnet pull force or even a higher net load intake (current one need to be limited).
#        Once you reach the money target (money spent), you get a higher level, which is saved, instead of deleting the player. 
#        the bigger level the harder it is to keep maintaining MagMed's battery since it's more powerfull.