
import random

def roll_dice():
    number = int(random.randint(1,6))
    return number



number = roll_dice()
print(number)

while number != 6:
        
    number = roll_dice()
    print(number)