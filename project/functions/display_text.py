import time

def flush_print(text,x,y):  #local function that takes str block and a range as variable to display text 1 letter each time.
    print()
    for i in range(x,y):  
        print(f"{text[i]}", end='', flush=True) #flush forces the printing as soon as it executed, doesn't wait for the whole loop.
        time.sleep(0.04)
    time.sleep(0.8)

def skip_it(title): #allows you to skip intro or instru.
    option = input(f"\nPress Enter to display the {title}, or type anyhing else to skip: ")
    if option == "":
        skip = False
    else:
        skip = True
    return skip


def intro_print():   #displays intro from inported text file.
    with open("project/text/intro.txt") as txt1:
        intro = txt1.read()
    skip = skip_it("introduction")
    if not skip:
        flush_print(intro,0,172)
        flush_print(intro,172,369)
        for i in range(369, 382):
            print(f"{intro[i]}", end='', flush=True)
            time.sleep(0.1)
        flush_print(intro,382,451)
        flush_print(intro,451,508)
        flush_print(intro,508,605)
        time.sleep(2)
    print("\n")
    
    return

def instru_print():  #displays intructions from inported text file
    with open("project/text/instructions.txt") as txt2:
        instr = txt2.read()
    skip = skip_it("instructions")
    if not skip:
        flush_print(instr,0,114)
        flush_print(instr,114,452)
        flush_print(instr,452,591)
        flush_print(instr,591,723)
        flush_print(instr,723,909)
        flush_print(instr,909,1205)
        flush_print(instr,1205,1293)
        flush_print(instr,1293,1547)
        time.sleep(4)
    print("\n")
    
    return