import random

def roll_dice(sides):
    result = random.randint(1,sides)
    return result
    
sides = int(input("Enter the number of the sides: "))

while True:
    result = roll_dice(sides)
    print(result)
    if result == sides:
        break
    # used if/break to avoid the double print