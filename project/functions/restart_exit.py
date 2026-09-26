from shared import *
from functions.menus_display import main_menu

def quit():
    game_over = input('Are you sure you want to quit?\nType "yes" to confirm or any other key to resume: ')
    game_over = game_over.lower()
    if game_over == "yes":
        print("All the metal have been recycled, Goodbye!")
        game_over = True
    else:
        game_over = False
    return game_over

def add_restart():
    if "[4] Restart" not in main_menu_list:
        main_menu_list.insert(3, "[4] Restart")
        main_menu_list[4] = "[5] Exit"
    return main_menu_list

def restart_game():
    restart = input('The progress will be lost, are you sure you want to restart?\nType "yes" to confirm or any other key to resume: ')
    if restart.lower() == "yes":
        roadside_net.items.clear() 
        beach_net.items.clear()
        lake_net.items.clear()
        print("All the metal have been recycled, Goodbye!")
        main_menu_list = ["[1] Play", "[2] Inventory", "[3] Settings", "[4] Exit"]
    else:
        main_menu()
    return restart