import time
won = "Congratulations, you won the game!"
print("\n\t\t\t\t", end='')
for i in range(34):
    
    print(f"{won[i]}", end='', flush = True)
    time.sleep(0.08)
time.sleep(2)
print("\n\t\t\t\t    The game will close now.")
time.sleep(2)
    