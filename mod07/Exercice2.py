
import random

def roll_dice(sides):
    number = int(random.randint(1,sides))
    return number

sides = int(input("How many sides do you want on your dice: "))

number = roll_dice(sides)
print(number)

while number < sides:
        
    number = roll_dice(sides)
    print(number)