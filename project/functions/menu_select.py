def display(menu_list):
    for menu in menu_list:
        print(f"\t\t\t\t{menu}")
    return
    
def choose_option():
    option = input("\nSelect an option or type 'lopeta' to exit: ")
    return option

def naming_item(weight, matter):
    name = input(f"\nYou found {weight:.1f}g of {matter}, name the item and press ENTER to collect it to the net: ")
    if name == "":
        name = matter[0].upper() + matter[1:]
    return name

def check_input(option, list):
    if option.isdigit():
        if int(option) > len(list) or int(option) < 0:
            print("Please select a valid option")
    elif option.isalpha():
        if option != "lopeta" and option != "":
            print("Please select a valid option")
    return