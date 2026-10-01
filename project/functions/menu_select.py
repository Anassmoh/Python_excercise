def display(menu_list):  #Displays menu lists.
    for menu in menu_list:
        print(f"\t\t\t\t{menu}")
    return
    
def choose_option(): #Return selected option from any menu.
    option = input("\nSelect an option or type 'lopeta' to exit: ")
    return option

def naming_item(weight, matter): #Allows you to name your litter, else it gives a standard matter label.
    name = input(f"\nYou found {weight:.1f}g of {matter}, name the item and press ENTER to collect it to the net: ")
    if name == "":
        name = matter[0].upper() + matter[1:] #Matter label
    return name

def check_input(option, list):  #Checks if option is in the range of the relevant list, also refuses weird inputs.
    if option.isdigit():
        if int(option) > len(list) or int(option) < 0:
            print("Please select a valid option")
    elif option.isalpha():
        if option != "lopeta" and option != "":
            print("Please select a valid option")
    return