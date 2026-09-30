def name_age():
    while True:
        name = input("Enter your name: ")    
        if name.isalpha():
            name = name[0].upper() + name[1:].lower()
            break
        else:
            print("Please Enter a valid name.\n") 
    while True:
        age = input("Enter your age: ")
        if not age.isdigit() or age == "":
            print("Please enter a valid age.\n")
        elif int(age) <= 0:
            print("Please enter a valid age.\n")
        else:
            break      
    return name, age

