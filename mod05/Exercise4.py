import random
number = random.randint(1,10)
guess = int(input("Guess a number (1-10): "))

while number != guess:
    if guess < number:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Guess a number (1-10): "))
print("Correct")