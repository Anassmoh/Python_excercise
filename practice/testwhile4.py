import time
battery = 100
def player():  
    print(f"{battery}% battery" )
    return




game_over = False

while not game_over:
    battery = 10
    time_stamp = time.time()
    while battery > 0:
        if time.time() - time_stamp > 1:
            battery -= 1
            time_stamp = time.time()
    else:
        game_over = True
        break

player()
player()
player()
player()
player()

