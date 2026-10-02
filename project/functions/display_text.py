import time

def intro_print():   #displays intro from inported text file.
    with open("project/text/intro.txt") as txt1:
        intro = txt1.read()

    print()
    for i in range(172):  # visuals.
        print(f"{intro[i]}", end='', flush=True)
        time.sleep(0.04)
    time.sleep(0.8)
    print()
    for i in range(172, 368):
        print(f"{intro[i]}", end='', flush=True)
        time.sleep(0.04)
    time.sleep(0.8)
    for i in range(368, 423):
        print(f"{intro[i]}", end='', flush=True)
        time.sleep(0.04)
    time.sleep(0.8)
    print()
    for i in range(423, 481):
        print(f"{intro[i]}", end='', flush=True)
        time.sleep(0.04)
    time.sleep(0.8)
    print()
    for i in range(481, 577):
        print(f"{intro[i]}", end='', flush=True)
        time.sleep(0.05)
    print("\n")
    time.sleep(2)
    return

def instru_print():  #displays intructions from inported text file
    with open("project/text/instructions.txt") as txt2:
        instr = txt2.read()

    print()
    for i in range(114):
        print(f"{instr[i]}", end='', flush=True)
        time.sleep(0.04)
    time.sleep(1.5)
    print()
    for i in range(114,452):
        print(f"{instr[i]}", end='', flush=True)
        time.sleep(0.04)
    time.sleep(1.5)
    print()
    for i in range(452,591):
        print(f"{instr[i]}", end='', flush=True)
        time.sleep(0.04)
    time.sleep(1.5)
    print()
    for i in range(591,723):
        print(f"{instr[i]}", end='', flush=True)
        time.sleep(0.04)
    time.sleep(1.5)
    print()
    for i in range(723,909):
        print(f"{instr[i]}", end='', flush=True)
        time.sleep(0.04)
    time.sleep(1.5)
    print()
    for i in range(909,1205):
        print(f"{instr[i]}", end='', flush=True)
        time.sleep(0.04)
    time.sleep(1.5)
    print()
    for i in range(1205,1293):
        print(f"{instr[i]}", end='', flush=True)
        time.sleep(0.04)
    time.sleep(1.5)
    print()
    for i in range(1293,1547):
        print(f"{instr[i]}", end='', flush=True)
        time.sleep(0.04)
    print("\n")
    time.sleep(6)