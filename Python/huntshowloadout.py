# This script is used by a discord bot to generate random loadout for the game Hunt Showdown 
# 11/07/2024 By Elewyn

# Prerequisite: random module
import random
choise = 'another'
# Set Loop
while not (choise == 'satisfied') :
# Menu
      print("""Hey hunter, running out of ideas for getting a loadout together?
      I've got something for you, but first let me ask you some questions:""")

# Settings
      wantmain = input("Do you want a main weapon?(yes or no)")

      wantsecondary = input("Do you want a secondary weapon?(yes or no)")

      wantmelee = input("Do you want a melee tool?(yes or no)")

      wantconsumables = input("How many consumables you you want?(0-4)")
      
# Clear
      import os
      clear = lambda: os.system('cls')
      clear()

# Roll main weapon if needed
      if wantmain == 'yes':
            main = random.choice(['Romero 77','Caldwell Rival 78','Springfield 1866','Winfield M1873','Winfield M1873C','Winfield M1876 Centennial','Vetterli 71 Karabiner','Martini-Henry IC1','Caldwell Marathon','Mako 1895 Carbine','Sparks LRR','Winfield 1887 Terminus','Winfield 1893 Slate','Drilling','Specter 1882','Berthier Mle 1892','Lebel 1886','Mosin-Nagant M1891','Crown & King Auto-5','Nitro Express Rifle','Railroad Hammer','Bomb Lance','Combat Axe','Katana','Crossbow','Bow'])
            print("your main weapon is: a",main)
      if wantmain == 'no':
            print("No main, no gain")

# Roll secondary weapon if needed
      if wantsecondary == 'yes':
            secondary = random.choice(['Nagant M1895','Caldwell Conversion Pistol','Caldwell 92 New Army','Caldwell Pax','LeMat Mark II Revolver','Bornheim No. 3','Scottfield Model 3','Dolch 96','Cavalry Saber','Baseball Bat','Machete','Hand Crossbow'])
            print("your secondary weapon is: a",secondary)
      if wantsecondary == 'no':
            print("You prefer the big ones?")

# Roll melee weapon if needed
      if wantmelee == 'yes':
            melee = random.choice(['Knife','Heavy knife','Dusters','Knuckle Knife','Throwing Axes','Throwing Knives','Throwing Spear'])
            print("your melee weapon is: a",melee)
      if wantmelee == 'no':
            print("You wanna fist fight?")

# Roll set number of consumables
      consumableslist = ['Ammo box', 'Medical Pack', 'Tool Box', 'Antidote Shot', 'Weak Antidote Shot', 'Regeneration Shot', 'Weak Regeneration Shot', 'Stamina Shot', 'Weak Stamina Shot', 'Vitality Shot', 'Weak Vitality Shot', 'Firebomb', 'Liquid Fire Bomb', 'Hellfire Bomb', 'Choke Beetle', 'Stalker Beetle', 'Fire Beetle', 'Chaos Bomb', 'Sticky Bomb', 'Poison Bomb', 'Hive Bomb', 'Flash Bomb', 'Concertina Bomb', 'Frag Bomb', 'Big Dynamite Bundle', 'Dynamite Bundle', 'Dynamite Stick', 'Waxed Dynamite Stick']

      match wantconsumables:
            case '0':
                  print("No consumables for you")
            case '1':
                  first = random.choice(consumableslist)
                  print("Your first consumable is: a",first)

            case '2':
                  first = random.choice(consumableslist)
                  print("Your first consumable is: a",first)
                  second = random.choice(consumableslist)
                  print("Your second consumable is: a",second)

            case '3':
                  first = random.choice(consumableslist)
                  print("Your first consumable is: a",first)
                  second = random.choice(consumableslist)
                  print("Your second consumable is: a",second)
                  third = random.choice(consumableslist)
                  print("Your third consumable is: a",third)

            case '4':
                  first = random.choice(consumableslist)
                  print("Your first consumable is: a",first)
                  second = random.choice(consumableslist)
                  print("Your second consumable is: a",second)
                  third = random.choice(consumableslist)
                  print("Your third consumable is: a",third)
                  fourth = random.choice(consumableslist)
                  print("Your Fourth consumable is: a",fourth)

# Ask if loadout is OK to leave the loop   
      choise = input("Satisfied? Or we go for another?(satisfied/another)")
 
      if choise == 'satisfied':
            exit
      if choise == 'another':
            keepsetting = input("keep same settings?(yes/no)")
            if keepsetting == 'no':
                  wantmain = 'unset'
                  wantsecondary = 'unset'
                  wantmelee = 'unset'
                  wantconsumables = 'unset'
                  
