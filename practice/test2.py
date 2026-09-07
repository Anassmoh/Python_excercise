import random
times = 0
total = 0



while times < 1000:
    dice1 = dice2 = rolls = 0
    while (dice1 != 6 or dice2 != 6):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        rolls += 1
    total += rolls
    times += 1
average = total / times

print(f"hte average is {average:6.2f}")       