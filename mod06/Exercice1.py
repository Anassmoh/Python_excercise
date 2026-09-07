import random

rolls = int(input("How many dice to roll: "))
sum = 0

for n in range(rolls):
    sum += random.randint(1,6)
print("Sum of the dice:", sum)