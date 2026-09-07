import random
rounds = 0
total_rolls = 0

while rounds < 100000:
    dice1 = dice2 = rolls = 0
    while (dice1 != 6 or dice2 != 6):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        rolls = rolls + 1
    #print(f"Rolled {rolls:d} times.")
    rounds = rounds + 1
    total_rolls = total_rolls + rolls

average_rolls = total_rolls/rounds
print(f"Average rolls required: {average_rolls:6.2f}")