import random

integer = random.randint(1,10)
print(integer)
number = int(input("Give a number (1-10): "))

while number != integer:
    if number < integer:
        print("Too low")
        
    elif number > integer:
        print("Too high")
    
    
    number = int(input("Give a number (1-10): "))
else:
    print("Correct")