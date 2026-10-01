import time

def measuring(): #Overwriting in the same line the measuring visuals.
    for i in range(2):
        print(f"\rMeasuring the item.                   ", end='')
        time.sleep(0.5)
        print(f"\rMeasuring the item..                  ", end='')
        time.sleep(0.5)
        print(f"\rMeasuring the item...                 ", end='')
        time.sleep(0.5)
    return

def manual_scrap():  #Overwriting in the same line the manual collecting when it's non-magnetic.
    for i in range(2):
        print(f"\rHand scrapping the item.   ", end='')
        time.sleep(0.5)
        print(f"\rHand scrapping the item..  ", end='')
        time.sleep(0.5)
        print(f"\rHand scrapping the item... ", end='')
        time.sleep(0.5)
    return
    
def demagnify():
    for i in range(2): #Overwriting in the same line the detaching from magnet, when it's magnetic.
        print(f"\rDetaching the item from the magnet.   ", end='')
        time.sleep(0.5)
        print(f"\rDetaching the item from the magnet..  ", end='')
        time.sleep(0.5)
        print(f"\rDetaching the item from the magnet... ", end='')
        time.sleep(0.5)
    return

def processing(): #visual 0% to 100%
    print("")
    for i in range(101):
        print(f"\rProcessing the items {i}%", end='')
        time.sleep(0.04)
    return