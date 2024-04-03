
# Set loop
option = 0
while not (option =='quit') :
    
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

    match option:
        case '1' :
            print("edit hideout upgrades")
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