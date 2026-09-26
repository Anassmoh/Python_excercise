import time
import random
from functions.restart_exit import add_restart
from classes.items_classes import Items

def magnet_fishing():
            main_menu_list = add_restart()
            for _ in range(random.randint(3,8)):
                time.sleep(0.5)
                print("\n0 μV")
            voltage = random.randint(1,150)
            for n in range(4):
                time.sleep(0.2)
                print(f"\n{voltage + random.randint(-2,2)} μV")
            magnetude = random.choice([True,False])
            if magnetude == True:
                weight = voltage * 1.5
                matter = "Iron"
                name = input(f"\n{voltage} μV! {voltage} μV! {voltage} μV!\n\nYou found {weight}g of {matter}, name the item and press ENTER to collect it to the net: ")
                litter = Items(name, voltage, weight, matter)
            else:
                weight = "N/A"
                if 0 < voltage <= 50:
                    matter = random.choice(["aluminum", "brass"])
                    name = input(f"\n{voltage} μV! {voltage} μV! {voltage} μV!\n\nYou found some {matter}, name the item and press ENTER to collect it to the net: ")
                    litter = Items(name, voltage, weight, matter)
                elif 50 < voltage <= 100:
                    matter = random.choice(["silver", "copper"])
                    name = input(f"\n{voltage} μV! {voltage} μV! {voltage} μV!\n\nYou found some {matter}, name the item and press ENTER to collect it to the net: ")
                    litter = Items(name, voltage, weight, matter)
                else:                            
                    matter = "gold"
                    name = input(f"\n{voltage} μV! {voltage} μV! {voltage} μV!\n\nCongratulations! You found some {matter}, name the item and press ENTER to collect it to the net: ")
                    litter = Items(name, voltage, weight, matter)    
            return litter
