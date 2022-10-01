# print('''
#                                                 (\n
#                                                  )       /\
#                                                (__      /%%\
#                                               |_I_|     /%%\
#                    __________________/',______|I_I|____/%%%%\/\
#                   /\'.__.'.__.'.__.'/\/_\'.__.'.__.'.__\%%%%/%%\
#                  /%%\_.'.__.'.__.'./\/_ _\_.'.__.'.__.'.\%%/%%%%\
#                 /%%%%\.__.'.__.'._/\/|_|_|\.__.'.__.'.__.\%/%%%%\   
#                 /%%%%\_.'.__.'.__.\/_|_|_|_\'.__.'.__.'.__\%%%%%%\                  
#                /%%%%%%\____________________________________\%%%%%%\
#               /%%%%%%%%\]== _ _ _ ============______======]%%%%%%%\
#               /%%%%%%%/\]==|_|_|_|============|////|======]%%%%%%%%\__
#            __/%%%%%%%/%%\==|_|_|_|============|////|======]%%%%%%%%\lc
#             /%%%%%%%/%%%%\====================|&///|======]%%%%%%%%%\
#             /%%%%%%%/%%%%\====================|////|======]^^^^^^^^^^
#            /%%%%%%%/%%%%%%\===================|////|======]  _ - _ -
#            /%%%%%%%/%%%%%%\"""""""""""""""""""'===='"""""""
#            ^^^^^^^/%%%%%%%%\   _ -   _ -              _-
#                   ^^^^^^^^^^               
# ''')
print("Welcome to the Forest of Forelorn Fates.")
print("You wake up in a pile of leaves, wearing a green hat, a ripped Christmas sweater, and pajama bottoms.\nThe cold bite of the mountain winds sends shivers down your spine. ") 
decision_1=input("Do you 'try to make a fire', 'call for help', or 'search for nearby landmarks'?\n").lower()
#Start Fire branch.
if decision_1=="try to make a fire":
  print("\nAll the nearby trees, leaves, and sticks are covered in a morning dew.\nPerhaps you can use your sweater fabric as kindling?")
  decision_2_fire=input("Do you 'tear apart sweater',\n'attempt to dry some of the surrounding material',\nor 'continue searching elsewhere'? ").lower()
  if decision_2_fire=="tear apart sweater":
    print("\nYou take your sweater off and start ripping it.\nTurns out, it is pretty difficult to break down the fabric into threads.\nYou exert all of your energy trying to make the kindling, and the sun begins to set.\nYou freeze to death as the snow begins to fall. GAME OVER.")
  elif decision_2_fire=="attempt to dry some of the surrounding material":
    print("\nYou gather wet leaves, sticks, and branches. You find an open area where the sun is shining.\nYou lay the material on some dry dirt and wait.\nAs the sun begins to set, you realize that waiting for sticks to dry was not the best survival strategy.\nSnow begins to fall, and you slowly freeze to death. GAME OVER.")
  elif decision_2_fire=="continue searching elsewhere":
    print("\nYou scramble up the side of a large rock to look at your surroundings.\nYou see a small cabin, a hunting blind, and a small cave in the face of a nearby cliff.")
    decision_2_landmarks=input("Do you investigate 'the cabin', 'the hunting blind', or 'the small cave'?\n").lower()
    #Start Fire->Cabin branch.
    if decision_2_landmarks=="the cabin":
      print('\nAs you approach the cabin, a man bursts through the front door.\nA pang of fear shoots through you, and you hide behind a small boulder.\nYou hear the man say,"I will find that little elf and RIP HIM TO SHREDS!"\nOnce the man leaves, you enter the cabin.\nOn the floor, you see a torn open present and coal chunks scattered over the floor.\nYou see serveral other useful items, but can only carry one.')
      decision_3_cabin=input("Do you take 'climbing gear', 'hunting rifle', or the 'longwave radio'?\n")
      if decision_3_cabin=="hunting rifle":
        print("\nYour small hands are unable to hold on to the rifle.\nIt slips from your grasp, falls to the ground, and fires a shot into your leg. You begin to bleed out. \nAs you exhale your last breath, you hear the evil man cackling as he locks the front door. \nGAME OVER.")
      elif decision_3_cabin=="longwave radio":
        print("\nYou leave the cabin and find an open field in the forest to use the radio.\nYou find the emergency frequency and send an S.O.S. signal.\nA helicopter comes and picks you up-but the rescuers are in awe.\nThey had never seen an elf before. The story of the abandoned elf spreads in the media.\nYou become a celebrity among humans and Santa faces child endangerment charges for his negligence. \nCONGRATULATIONS! YOU WIN!")
      elif decision_3_cabin=="climbing gear":
        print("\nYou carry the climbing gear on your back and return to the cave. You slowly climb up the side of the cliff and enter the cave.\nInside, you find the skeleton of a soldier wearing a paratrooper survival kit.\nInside, you find a red flares, food, water, and a loaded hangun.\nYou remember from elf training camp that igniting your elven hair emits magical light that can only be seen by reindeer.\nYou tie your hair to the flare and shoot it into the air. Santa Claus appears and takes you back to the North Pole.\n CONGRATULATIONS, YOU WIN!")
      else:
        print("\nYou cannot find the item and take too long to exit the cabin.\nThe killer returns, stunned that you made the hunt so easy for him. \nHe stuffs the coal down your throat and you die from suffocation. GAME OVER.")
    elif decision_2_landmarks=="the hunting blind":
      print('\nYou climb into the hunting blind, hopeful to find a weapon or supplies.\nYou find a crate of ammunition and foodstuffs, but no weapon.\nAs you try to stuff some granola bars into your pocket, the entrance flap rustles and a man steps through.\n"You sure did make this easy for me, you little shit. COME HERE!"\nYou are pinned to the ground by the ferocious fiend and are torn to shreds with iron bear claws.\nGAME OVER.')
    elif decision_2_landmarks=="the small cave":
      print('As you approach the bottom of the cliff, you realize that the cave is much higher than you thought it was.\nWith snow beginning to fall and the sun disappearing over the horizon, your only choice is to stay at the bottom and use the cliff overhang as shelter.\nYou curl up into a ball and begin to fall asleep.\nYou awake, suddenly, to a strange cackling laugh far above you.\n"MERRY CHRISTMAS, YOU ROTTEN LITTLE ELF!", a man screams as he presses a detonator.\nAn explosion breaks off a massive piece of rock, crushing you before you can move. GAME OVER.')
    else:
      print("\nAn overwhelming dread causes you to collapse to the ground. You realize that you should have trusted your initial choices. GAME OVER.")
    #End Fire->Cabin branch.
  else:
    print("\nAn overwhelming dread causes you to collapse to the ground. You realize that you should have trusted your initial choices. GAME OVER.")
#Start Call For Help branch.
elif decision_1=="call for help":
  print("\nYou scream as loud as you can for several minutes.\nAfter your voice finally gives out, a flash of black bursts from the underbrush and you are knocked to the ground.\nA malevolent figure towers above you, wearing tattered hunting gear, iron bear claws, and a wicked smile.\nIt laughs maniacally as it shreds you to pieces. GAME OVER.")
#Complete Call For Help branch.
#Start Landmark branch.
elif decision_1=="search for nearby landmarks":
  print("\nYou scramble up the side of a large rock to look at your surroundings.\nYou see a small cabin, a hunting blind, and a small cave in the face of a nearby cliff.")
  decision_2_landmarks=input("Do you investigate 'the cabin', 'the hunting blind', or 'the small cave'?\n").lower()
# #Start Cabin branch.
  if decision_2_landmarks=="the cabin":
    print('\nAs you approach the cabin, a man bursts through the front door.\nA pang of fear shoots through you, and you hide behind a small boulder.\nYou hear the man say,"I will find that little elf and RIP HIM TO SHREDS!"\nOnce the man leaves, you enter the cabin.\nOn the floor, you see a torn open present and coal chunks scattered over the floor.\nYou see serveral other useful items, but can only carry one.')
    decision_3_cabin=input("Do you take 'climbing gear', 'hunting rifle', or the 'longwave radio'?\n")
    if decision_3_cabin=="hunting rifle":
      print("\nYour small hands are unable to hold on to the rifle.\nIt slips from your grasp, falls to the ground, and fires a shot into your leg. You begin to bleed out. \nAs you exhale your last breath, you hear the evil man cackling as he locks the front door. \nGAME OVER.")
    elif decision_3_cabin=="longwave radio":
      print("\nYou leave the cabin and find an open field in the forest to use the radio.\nYou find the emergency frequency and send an S.O.S. signal.\nA helicopter comes and picks you up-but the rescuers are in awe.\nThey had never seen an elf before. The story of the abandoned elf spreads in the media.\nYou become a celebrity among humans and Santa faces child endangerment charges for his negligence. \nCONGRATULATIONS! YOU WIN!")
    elif decision_3_cabin=="climbing gear":
      print("\nYou carry the climbing gear on your back and return to the cave. You slowly climb up the side of the cliff and enter the cave.\nInside, you find the skeleton of a soldier wearing a paratrooper survival kit.\nInside, you find a red flare, food, water, and a loaded hangun.\nYou remember from elf training camp that igniting your elven hair emits magical light that can only be seen by reindeer.\nYou tie your hair to the flare and shoot it into the air. Santa Claus appears and takes you back to the North Pole.\n CONGRATULATIONS, YOU WIN!")
    else:
      print("\nYou cannot find the item and take too long to exit the cabin.\nThe killer returns, stunned that you made the hunt so easy for him. \nHe stuffs the coal down your throat and you die from suffocation. GAME OVER.")
# #Complete Cabin Branch
  elif decision_2_landmarks=="the hunting blind":
    print('\nYou climb into the hunting blind, hopeful to find a weapon or supplies.\nYou find a crate of ammunition and foodstuffs, but no weapon.\nAs you try to stuff some granola bars into your pocket, the entrance flap rustles and a man steps through.\n"You sure did make this easy for me, you little shit. COME HERE!"\nYou are pinned to the ground by the ferocious fiend and are torn to shreds with iron bear claws.\nGAME OVER.')
  elif decision_2_landmarks=="the small cave":
    print('As you approach the bottom of the cliff, you realize that the cave is much higher than you thought it was.\nWith snow beginning to fall and the sun disappearing over the horizon, your only choice is to stay at the bottom and use the cliff overhang as shelter.\nYou curl up into a ball and begin to fall asleep.\nYou awake, suddenly, to a strange cackling laugh far above you.\n"MERRY CHRISTMAS, YOU ROTTEN LITTLE ELF!", a man screams as he presses a detonator.\nAn explosion breaks off a massive piece of rock, crushing you before you can move. GAME OVER.')
  else:
    print("\nAn overwhelming dread causes you to collapse to the ground. You realize that you should have trusted your initial choices. GAME OVER.")
#Complete landmark branch
else:
  print("\nAn overwhelming dread causes you to collapse to the ground. You realize that you should have trusted your initial choices. GAME OVER.")

