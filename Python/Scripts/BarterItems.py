# Welcome to my first ever python script 
# This script is a stach&hideout management tool for the video game "Escape from tarkov"

# Set loop
option = 0
while not (option =='quit') :
    import os
    clear = lambda: os.system('clear')
    clear()
    
    #  Menu
    print("""hello, here is a quick script to count the barter items required for your hideout in Escacre From Tarkov
    (source: https://escapefromtarkov.fandom.com/)
    - If you want to edit your hideout type 1
    - If you want to see the quantity of an item required type 2
    - If you want to add an item to your stash, type 3
    - If you want to remove an item from your stash, type 4
    - If you want to leave, type quit""")

    # Ask 

    option = input("what are we doing today? ")
    
    # Set empty variables 
    medstationlevel = 0
    lavatorylevel = 0
    securitylevel = 0
    ventslevel = 0
    heatinglevel = 0
    workbenchlevel = 0
    illuminationlevel= 0
    watercollectorlevel = 0
    generatorlevel = 0
    restpacelevel = 0
    stachlevel = 0
    nutritionunitlevel = 0
    intelligencecenterlevel = 0
    shootingrangelevel = 0
    halloffamelevel = 0
    weaponstandlevel = 0
    scavcaselevel = 0
    bitcoinfarmlevel = 0
    airfilteringunitlevel = 0
    boozegeneratorlevel = 0
    librarylevel = 0
    solarpowerlevel = 0
    
    match option:
        case '1' :
            print("editing hideout state")
            print("medstation is level", medstationlevel
            )
            hideoutmodule = input ("type the name of the module: ")
            upgradelevel = input ("level of the module: ")

            input ("press a a key to continue")
        case '2' :
            itemtolist = input ("name of the item you want to list? ")
            print("you still need x", itemtolist)
        
            input ("press a a key to continue")
        case '3' :
            numberofitem = input ("how many of said item do you want to add? ")
            itemtoadd = input ("name of the desired item? ")
            print("added", numberofitem , itemtoadd)
            input ("press a a key to continue")
        case '4' :
            numberofitem = input ("how many of said item do you want to remove? ")
            itemtoremove = input ("name of the desired item? ")
            print("removed", numberofitem , itemtoremove)
            input ("press a a key to continue")
        case 'quit' :
            exit
