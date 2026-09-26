
from classes.items_classes import Items, RoadsideItems, BeachItems, LakeItems
from functions.active_magnet_fishing import *
from functions.input_check import *
from functions.menus_display import *
from functions.restart_exit import *

main_menu_list = ["[1] Play", "[2] Inventory", "[3] Settings", "[4] Exit"]
roadside_net = RoadsideItems()
beach_net = BeachItems()
lake_net = LakeItems()
name, age = name_age()

# TODO: this breaks when age string
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
            game_over = setting_menu()
        elif main_menu_option == "4":
            if "[4] Restart" in main_menu_list:
                restart = restart_game()
                if restart == "yes":
                    break
            else:
                game_over = quit()
        elif main_menu_option == "5" or main_menu_option == "lopeta":
            game_over = quit()
    if game_over == True:
        break        
    elif restart == "yes":
        name, age = name_age()
else: 
    if int(age) < 12:
        print("Your age doesn't meet the minimum required, the game will exit immediately!")



