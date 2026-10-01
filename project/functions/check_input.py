def name_age():
    while True: #Loops till name is alphabet.
        name = input("Enter your name: ")    
        if name.isalpha():  
            name = name[0].upper() + name[1:].lower() #Return correct name casing.
            break
        else:
            print("Please Enter a valid name.\n") 
    while True: #Loops till age is digit.
        age = input("Enter your age: ")
        if not age.isdigit() or age == "":
            print("Please enter a valid age.\n")
        elif int(age) <= 0:
            print("Please enter a valid age.\n")
        else:
            break      
    return name, age

