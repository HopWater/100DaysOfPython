print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = (input("Do you want to go left or right? "))

#If left continue, if not left end game.

if direction == "left":
    wait = (input("Do you want to swim or wait? "))

    #If wait continue, else end game.
    if wait == "wait":

        door = (input("Good choice\nWhat door do you want to pick?\nRed, Yellow or Blue? "))

        # Yellow door to win game, else Game over.
        if door == "Red" or door == "red":
            print("Burned by fire.\nGame Over.")

        elif door == "Blue" or door == "blue":
            print("Eatan by beasts.\nGame Over.")

        elif door == "Yellow" or door == "yellow":
            print("You Win!")

        else:
            print("Game Over.")


    else:
        print("Attacked by trout.\nGame Over.")


else:
    print("Fall into a hole.\nGame Over.")