import random

rolls = int(input("How many dice to roll: "))

sum = 0
for roll in range(rolls):
   num = random.randint(1,6)
   sum = sum + num


print("Sum of the dice:", sum)


   
    
