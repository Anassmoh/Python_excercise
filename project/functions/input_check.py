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

def choose_option():
    option = input("\nSelect an option or type 'lopeta' to exit: ")
    return option

def check_input(option, list):
    if option == "lopeta" or option == "":
        pass
    elif int(option) > len(list) or int(option) < 0:
        print("invalid input")
    return