
def treasure_island_end() -> None:
    print('''
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
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
    step_01 = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\": ")
    if step_01[0].lower() == "l":
        # step_02
        step_02 = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ")
        if step_02[0].lower() == "w":
            # step_08
            print("You get attacked by an angry trout. Game Over.")
        else:
            step_03 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? Type  \"Red\", \"Yellow\" or \"Blue\". ")
            if step_03[0].lower() == "r":
                #step_05
                print("You found the treasure! You Win!")
            elif step_03[0].lower() == "y":
                # step_06
                print("You enter a room of beasts. Game Over.")
            else: # step_03 == "Blue"
                # step_07
                print("You chose a door that doesn't exist. Game Over.")
    else:
        # step_09
        print("You fell into a hole. Game Over.")
        
    

if __name__ == "__main__":
    treasure_island_end()
