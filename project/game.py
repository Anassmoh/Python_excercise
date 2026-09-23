import random
import time

main_menu_list = ["[1] Play", "[2] Inventory", "[3] Settings", "[4] Exit"]
#TODO: this is a Tuple so can use all net to unpack better
roadside_net, beach_net, lake_net = [], [], []

# TODO: add list for instances as i dont know the objects
class AllNet:
    item_count = 0
    all_net = []
    def __init__(self, name, voltage, weight, matter):
        AllNet.all_net.append(self)
        self.name = name
        self.voltage = voltage
        self.weight = weight
        self.matter = matter

    def collect_print(self):
        print(f"{self.name}: {self.voltage} {self.weight} {self.matter}")

class RoadsideNet(AllNet):
    def __init__(self, name, voltage, weight, matter):
        super().__init__(name, voltage, weight, matter)

class BeachNet(AllNet):
    def __init__(self, name, voltage, weight, matter):
        super().__init__(name, voltage, weight, matter)

class LakeNet(AllNet):
    def __init__(self, name, voltage, weight, matter):
        super().__init__(name, voltage, weight, matter)



def name_age():
    while True:
        name = input("Enter your name: ")
        if name == "":
            print("invalid input")
        else:
            name = name[0].upper() + name[1:].lower()
            break
    while True:
        age = input("Enter your age: ")
        if age == "":
            print("invalid input")
        else:
            break
    return name, age

def display(menu_list):
    for menu in menu_list:
        print(menu)
    return

def choose_option():
    option = input("\nSelect an option or type 'lopeta' to exit: ")
    return option

def check_input(option, list):
    if option == "lopeta" or option == "":
        pass
    elif int(option) > len(list) or int(option) < 0:
        print("invalid input")
    return

# TODO: figure out how to avoid override the object
def magnet_fishing(net):
    while True:
        cast = input("Press ENTER to cast your magnet or type any other key to change the map: ")
        if cast != "":
            play_menu()
            main_menu_list = add_restart()
            break
        else:
            for _ in range(random.randint(3,8)):
                time.sleep(0.5)
                print("\n0 μV")
            voltage = random.randint(1,150)
            for n in range(4):
                time.sleep(0.2)
                print(f"\n{voltage - 4 + n} μV")
            magnetude = random.choice([True,False])
            if magnetude == True:
                weight = voltage * 1.5
                matter = "Iron"
                metal_litter = input(f"\n{voltage} μV! {voltage} μV! {voltage} μV!\n\nYou found {weight}g of {matter}, name the item and press ENTER to collect it to the net: ")
            else:
                weight = "N/A"
                if 0 < voltage <= 50:
                    matter = random.choice(["aluminum", "brass"])
                    metal_litter = input(f"\n{voltage} μV! {voltage} μV! {voltage} μV!\n\nYou found some {matter}, name the item and press ENTER to collect it to the net: ")
                elif 50 < voltage <= 100:
                    matter = random.choice(["silver", "copper"])
                    metal_litter = input(f"\n{voltage} μV! {voltage} μV! {voltage} μV!\n\nYou found some {matter}, name the item and press ENTER to collect it to the net: ")
                else:                            
                    matter = "gold"
                    metal_litter = input(f"\n{voltage} μV! {voltage} μV! {voltage} μV!\n\nCongratulations! You found some {matter}, name the item and press ENTER to collect it to the net: ")
            roadside_net.append(RoadsideNet(metal_litter, voltage, weight, matter))
            
            
    return

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
        main_menu_list = ["[1] Play", "[2] Inventory", "[3] Settings", "[4] Exit"]
    else:
        pass
    return restart

def quit():
    exit = input('Are you sure you want to quit?\nType "yes" to confirm or any other key to resume: ')
    exit = exit.lower()
    if exit == "yes":
        print("All the metal have been recycled, Goodbye!")
    else:
        pass
    return exit

def main_menu():
    print("\nMAIN MENU\n")
    display(main_menu_list)
    main_menu_option = choose_option()
    check_input(main_menu_option, main_menu_list)
    return main_menu_option

def play_menu():
    play_menu_list = ("[1] Roadside", "[2] Beach", "[3] Lake", "[4] Main menu", "[5] Exit")
    print("\nSELECT A MAP\n")
    display(play_menu_list)
    map_option = choose_option()
    check_input(map_option, play_menu_list)
    if map_option == "1":
            magnet_fishing(roadside_net)
    elif map_option == "2":
        magnet_fishing(beach_net)
    elif map_option == "3":
        magnet_fishing(lake_net)
    elif map_option == "4":
        pass
    elif map_option == "5" or map_option == "lopeta":
        exit = quit()
        return exit

def inventory_menu():
    inventory_menu_list = ("[1] All the nets ", "[2] Roadside net", "[3] Beach net", "[4] Lake net", "[5] Main menu", "[6] Exit") 
    print("\nSELECT A NET\n")
    display(inventory_menu_list)
    inventory_option = choose_option()
    check_input(inventory_option, inventory_menu_list)
    if inventory_option == "1" :
        print("\nThis is all your catch so far:\n")
        print()
        if len(roadside_net) == 0:
            print("Roadside net : Empty")
        else:
            for item in roadside_net:
                print({item.name})
        if len(beach_net) == 0:
            print("Beach net : Empty")
        else:
            for item in beach_net:
                print(item.name)
        if len(lake_net) == 0:
            print("Lake net : Empty")
        else:
            for item in lake_net:
                print(item.name)    
    elif inventory_option == "2":
        if len(roadside_net) == 0:
            print("Your roadside net is empty")
        else:
            print("\nThis is your roadside catch so far:\n")
            for item in roadside_net:
                print(item.name)
    elif inventory_option == "3":
        if len(beach_net) == 0:
            print("Your beach net is empty")
        else:
            print("\nThis is your beach catch so far:\n")
            for item in beach_net:
                print(item.name)
    elif inventory_option == "4":
        if len(lake_net) == 0:
            print("Your lake net is empty")
        else:
            print("\nThis is your lake catch so far:\n")
            for item in lake_net:
                print(item.name)
    elif inventory_option == "5":
        pass
    elif inventory_option == "6" or inventory_option == "lopeta":
        exit = quit()
        return exit

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
            exit = quit()
    elif setting_option== "3":
        pass
    elif setting_option == "4" or setting_option == "lopeta":
        exit = quit()
        return exit





name, age = name_age()

# TODO: this breaks when age string
while int(age) >= 12:
    print(f"\n{name}, {age} years old.\n\nHello {name}, welcome to MagNet!")
    while True:
        main_menu_option = main_menu()
        if main_menu_option == "1":
            exit = play_menu()
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

#need to add uv to detect differents stuff 
#add also 
 #x = random.randint(0,150)
#for i in range(x-3,x+1):
#    print(i)
#print(f"{x}\n{x}") 
#import time
#import random



#for x in range(random.randint(3,8)):
#    time.sleep(0.7)
#    print(x)
