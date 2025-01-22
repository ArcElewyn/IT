# This script is used by a discord bot to generate random loadout for the game Hunt Showdown 
# 11/07/2024 By Elewyn

# Prerequisite: random module

import random
import os
clear = lambda: os.system('cls')
clear()

# Set Loop
choise = 'unset'
while not (choise == 'n') :
      print("""Hey hunter, running out of ideas for getting a loadout together?
      I've got something for you, but first let me ask you some questions:""")

# Settings
      wantmain = input("Do you want a main weapon?(y/n)") 
      if wantmain == 'y':
            mainammo = input("Do you wanna use special ammo?(y/n)")
            meleemain = input("Are melee primary included?(y/n)") 
            if meleemain == 'y':
                   mainchoice = ['Romero 77','Caldwell Rival 78','Springfield 1866','Winfield M1873','Winfield M1873C','Winfield M1876 Centennial','Vetterli 71 Karabiner','Martini-Henry IC1','Caldwell Marathon','Mako 1895 Carbine','Sparks LRR','Winfield 1887 Terminus','Winfield 1893 Slate','Drilling','Specter 1882','Berthier Mle 1892','Lebel 1886','Mosin-Nagant M1891','Crown & King Auto-5','Nitro Express Rifle','Railroad Hammer','Bomb Lance','Combat Axe','Katana','Crossbow','Bow']
            if meleemain == 'n':
                  mainchoice = ['Romero 77','Caldwell Rival 78','Springfield 1866','Winfield M1873','Winfield M1873C','Winfield M1876 Centennial','Vetterli 71 Karabiner','Martini-Henry IC1','Caldwell Marathon','Mako 1895 Carbine','Sparks LRR','Winfield 1887 Terminus','Winfield 1893 Slate','Drilling','Specter 1882','Berthier Mle 1892','Lebel 1886','Mosin-Nagant M1891','Crown & King Auto-5','Nitro Express Rifle','Crossbow','Bow']

      wantsecondary = input("Do you want a secondary weapon?(y/n)")
      if wantsecondary == 'y':
            secondaryammo = input("Do you wanna use special ammo?(y/n)")
            meleesecondary = input("Are melee secondary included?(y/n)")
            if meleesecondary == 'y':
                  secondarychoice = ['Nagant M1895','Caldwell Conversion Pistol','Caldwell 92 New Army','Caldwell Pax','LeMat Mark II Revolver','Bornheim No. 3','Scottfield Model 3','Dolch 96','Cavalry Saber','Baseball Bat','Machete','Hand Crossbow']
            if meleesecondary == 'n':
                  secondarychoice = ['Nagant M1895','Caldwell Conversion Pistol','Caldwell 92 New Army','Caldwell Pax','LeMat Mark II Revolver','Bornheim No. 3','Scottfield Model 3','Dolch 96','Hand Crossbow'] 

      wantmelee = input("Do you want a melee tool?(y/n)")

      wantconsumables = input("How many consumables you you want?(0-4)")
     
# Clear     
      clear()

# Loop Roll
      keepsetting = 'unset'
      while not (keepsetting == 'no') :
                        
# Roll main weapon if needed
                        if wantmain == 'y':
                              mainweapon = random.choice(mainchoice)
                              print("your main weapon is: a",mainweapon )
                              if mainammo == 'y': # Roll special ammo if needed
                                    mainammotype = 'unset'
                                    match mainweapon:
                                          case 'Romero 77':
                                                mainammotype = random.choice(['Starshell','Dragonbreath','Pennyshot','Slug'])
                                          case 'Caldwell Rival 78':
                                                mainammotype = random.choice(['Flechette','Dragonbreath','Pennyshot','Slug'])
                                          case 'Springfield 1866':
                                                mainammotype = random.choice(['Dumdum','Poison','Explosive','High Velocity'])
                                          case 'Winfield M1873':
                                                mainammotype = random.choice(['Incendiary','Poison','High Velocity','Full Metal Jacket'])
                                          case 'Winfield M1873C':
                                                mainammotype = random.choice(['Incendiary','Poison','High Velocity','Full Metal Jacket'])
                                          case 'Winfield M1876 Centennial':
                                                mainammotype = random.choice(['Dumdum','Poison','High Velocity','Full Metal Jacket'])
                                          case 'Vetterli 71 Karabiner':
                                                mainammotype = random.choice(['Incendiary','High Velocity','Full Metal Jacket'])
                                          case 'Martini-Henry IC1':
                                                mainammotype = random.choice(['Incendiary','Explosive','Full Metal Jacket'])
                                          case 'Caldwell Marathon':
                                                mainammotype = random.choice(['Poison','Full Metal Jacket'])
                                          case 'Mako 1895 Carbine':
                                                mainammotype = random.choice(['Explosive','Full Metal Jacket'])
                                          case 'Sparks LRR':
                                                mainammotype = random.choice(['incendiary','Poison','Full Metal Jacket'])
                                          case 'Winfield 1887 Terminus':
                                                mainammotype = random.choice[('Flechette','Pennyshot','Slug')]
                                          case 'Winfield 1893 Slate':
                                                mainammotype = random.choice(['Pennyshot','Slug'])
                                          case 'Drilling':
                                                mainammotype = random.choice(['Dumdum','Full Metal Jacket','Pennyshot','Slug'])
                                          case 'Specter 1882':
                                                mainammotype = random.choice(['Flechette','Dragonbreath','Pennyshot','Slug'])
                                          case 'Berthier Mle 1892':
                                                mainammotype = random.choice(['Incendiary','Spitzer'])
                                          case 'Lebel 1886':
                                                mainammotype = random.choice(['Incendiary','Spitzer'])
                                          case 'Mosin-Nagant M1891':
                                                mainammotype = random.choice(['Incendiary','Spitzer'])
                                          case 'Crown & King Auto-5':
                                                mainammotype = random.choice(['Flechette','Pennyshot','Slug'])
                                          case 'Nitro Express Rifle':
                                                mainammotype = random.choice(['Shredder','Explosive'])
                                          case 'Bomb Lance':
                                                mainammotype = random.choice(['Dragon Breath','Steel Ball','Waxed Frag'])
                                          case 'Crossbow':
                                                mainammotype = random.choice(['Shot Bolt','Explosive Bolt'])
                                          case 'Bow':
                                                mainammotype = random.choice(['Poison Arrow','Concertina Arrow','Frag Arrow'])
                                          case _:
                                                print("No special ammo for this weapon") 
                                    print("your special ammo is",mainammotype )
                        if wantmain == 'n':
                              print("No main, no gain")

# Roll secondary weapon if needed
                        if wantsecondary == 'y':
                              secondaryweapon = random.choice(secondarychoice)
                              print("your secondary weapon is: a",secondaryweapon )
                              if secondaryammo == 'y': # Roll special ammo if needed
                                    secondaryammotype = 'unset'
                                    match secondaryweapon:
                                          case 'Nagant M1895':
                                                secondaryammotype = random.choice(['Dumdum','Poison','High Velocity'])
                                          case 'Caldwell Conversion Pistol':
                                                secondaryammotype = random.choice(['Dumdum','Full Metal Jacket'])
                                          case 'Caldwell 92 New Army':
                                                secondaryammotype = random.choice(['Dumdum','Full Metal Jacket'])
                                          case 'Caldwell Pax':
                                                secondaryammotype = random.choice(['Incendiary','Dumdum','Poison','Full Metal Jacket','High Velocity'])
                                          case 'LeMat Mark II Revolver':
                                                secondaryammotype = random.choice(['Starshell','Incendiary','Dragon Breath','Full Metal Jacket','Slug'])
                                          case 'Bornheim No. 3':
                                                secondaryammotype = random.choice(['Incendiary','High Velocity'])
                                          case 'Scottfield Model 3':
                                                secondaryammotype = random.choice(['Full Metal Jacket','Dumdum','Incendiary','High Velocity'])
                                          case 'Dolch 96':
                                                secondaryammotype = random.choice(['Dumdum','Full Metal Jacket'])
                                          case 'Hand Crossbow':
                                                secondaryammotype = random.choice(['Choke Bolt','Poison Bolt','Chaos Bolt','Dragon Bolt'])
                                          case _:
                                                print("No special ammo for this weapon")
                                    print("your special ammo is",secondaryammotype )
                        if wantsecondary == 'n':
                               print("You prefer the big ones?")

# Roll melee weapon if needed
                        if wantmelee == 'y':
                              melee = random.choice(['Knife','Heavy knife','Dusters','Knuckle Knife','Throwing Axes','Throwing Knives','Throwing Spear'])
                              print("your melee weapon is: a",melee)
                        if wantmelee == 'n':
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
                        choise = input("Go again?(y/n)")
                        if choise == 'n':
                              break
                        elif choise == 'y':
                              keepsetting = input("keep same settings?(y/n)")
                              if keepsetting == 'y':
                                    clear()
                              if keepsetting == 'n':
                                    wantmain = 'unset'
                                    wantsecondary = 'unset'
                                    wantmelee = 'unset'
                                    wantconsumables = 'unset'
                                    clear()
                                    break
