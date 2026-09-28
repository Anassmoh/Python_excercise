def display(menu_list):
    for menu in menu_list:
        print(menu)
    return
    
def choose_option():
    option = input("\nSelect an option or type 'lopeta' to exit: ")
    return option

def check_input(option, list):
    if option.isdigit():
        if int(option) > len(list) or int(option) < 0:
            print("Please select a valid option")
    elif option.isalpha():
        if option != "lopeta" or option != "":
            print("Please select a valid option")
    return
