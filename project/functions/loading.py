import time

def measuring():
    for i in range(2):
        print(f"\rMeasuring the item.                   ", end='')
        time.sleep(0.5)
        print(f"\rMeasuring the item..                  ", end='')
        time.sleep(0.5)
        print(f"\rMeasuring the item...                 ", end='')
        time.sleep(0.5)
    return

def manual_scrap():
    for i in range(2):
        print(f"\rHand scrapping the item.   ", end='')
        time.sleep(0.5)
        print(f"\rHand scrapping the item..  ", end='')
        time.sleep(0.5)
        print(f"\rHand scrapping the item... ", end='')
        time.sleep(0.5)
    return
    
def demagnefy():
    for i in range(2):
        print(f"\rDetaching the item from the magnet.   ", end='')
        time.sleep(0.5)
        print(f"\rDetaching the item from the magnet..  ", end='')
        time.sleep(0.5)
        print(f"\rDetaching the item from the magnet... ", end='')
        time.sleep(0.5)
    return

def processing():
    print("")
    for i in range(101):
        print(f"\rProcessing the items {i}%", end='')
        time.sleep(0.04)
    return