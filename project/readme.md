# MagNet

**Anass Mohattan**

MagNet is a text advanture game suitable for age 12+.

You just watched dozens of combat engineers retrieving land mines, they have been burried for last 70 years in an area that you once thought you knew so well. You rush to the basement looking for a specific unfinished project. As your peers direct their questions to the village seniors, they can hear the buzzing sound of your welding machine, your project was missing a need to become an invention .. "MagMed!" you said quietly while carving the name into the pipe. MagMed! a home made metal detector fused with a magnet and equipped with a 9V battery.

Your mission is to sweep the area from all kind of metal, you can choose to play in three different litter zones, each has its own MagNet - reinforced heavy-duty nets made specifically to resist sharp and corroded metal.

MagMed will detect any conductive metal on the way, once the electromagnetic field disturbed, hold your position, scrap the ground and measure the item's weight, if it's iron the magnet will pull it for you.

Label your item, and collect it to the relevant MagNet, unlabelled items will be given their matter as the name.
You can never put the litter back, regardless of its matter, state or weight.

You can view each Magnet content or you whole catch from the inventory menu. Once it starts to be filled, recycle it in the recycling center, you will receive an income based on the total weight of each matter.

Primarly, your mission is to clean your area from all the hazards and promote a sustainable lifestyle. Additionally, an income of 2500 markka is set for you as a daily goal.

MagMed is equipped with a 9V battery, which is draining 1% to 3% everytime you cast it, you may not be able to reach your daily goal with one charge, a low battery message will indicate that you need to soon quit the game after recycling, to allow the battery to charge, also to save your progress, which can only be done by properly exiting the game.

A full battery drain or a unpropper game disruption will lead to a loss of progress, including the income made during that round. In the other hand Restarting the game will result in your account being deleted.

Regardless of how the game was terminated, any non-recycled item left behind will be automatically recycled without any income in return.

After recharging your battery, enter your name and age and carry on from your latest saving checkpoint. Once the target reached, you will be greeted and appreciated for your environmental contribution, and the system will recycle your account..

The game will be developped in the future, the update will include:
-Player levels.
-Upgrades for MagMed.(pull force, depth detecting, surface area, bigger MagNet intake, battery life...)
-Hazardous finds that will block the game forcing you to immediately recycle.
-Instant battery recharge for a fee.
-Underwater magnet fishing.
-Sand sifter to filter the sand while battery is being charged 0.2% per sec.
-Utilizing some findings in in maintaining MagMed. (scews, bolts, springs...)
-Rare coin collection exhibit.

-------------------------------------------------------------------------------------------------------------------

AI have been used to:
Learn new python features.
Study whether some features exist (overwriting in terminal)
Discover built in alternatives (golbal, flush..)
Learn about metal detectors

-------------------------------------------------------------------------------------------------------------------

Folder scheme:

project
    │   game.py                                      #The main code where the game resides.
    │   readme.md                                    #This file.
    │   save_checkpoint.txt                          #json file where the game progress is saved
    │   
    ├───classes
    │   │   items.py                                 #File that has all the classes
    │   │   __init__.py                              #Empty (for python to treat as package)
    │   │   
    │   └───__pycache__
    │           items.cpython-314.pyc
    │           __init__.cpython-314.pyc
    │           
    ├───functions
    │   │   check_input.py                           #File that has input check functions
    │   │   display_text.py                          #File that has display intro and instruction functions
    │   │   loading.py                               #File that has visual print functions
    │   │   menu_select.py                           #File that has display and return functions
    │   │   __init__.py                              #Empty (for python to treat as package)
    │   │   
    │   └───__pycache__
    │           check_input.cpython-314.pyc
    │           display_text.cpython-314.pyc
    │           input_check.cpython-314.pyc
    │           loading.cpython-314.pyc
    │           Menu_printNchoose.cpython-314.pyc
    │           menu_select.cpython-314.pyc
    │           test.cpython-314.pyc
    │           user_bridge.cpython-314.pyc
    │           __init__.cpython-314.pyc
    │           
    ├───text
    │       instructions.txt                        #instruction block
    │       intro.txt                               #introduction block
    │       
    └───__pycache__
            game.cpython-314.pyc