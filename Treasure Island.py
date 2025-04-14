print("Welcome to Treasure Island.\nYou are trapped on an island.\nYour mission is to find the treasure.\nWhere do you wanna go?")
choice1 = input("Type 'left' or 'right': ").lower()

if choice1 == "left":
    choice2 = input("You reach a lake.\nThere is an island in the lake.\nType 'wait' to wait for a boat or 'swim' to swim across: ").lower()

    if choice2 == "wait":
        choice3 = input('You arrive at a house with three doors. One red, one yellow, and one blue.\nWhich color do you choose? Type "red", "yellow", or "blue": ').lower()
        
        if choice3 == "red":
            print("Game Over. You were burned by fire.")
        elif choice3 == "yellow":
            print("You win! You found the treasure! 🏆")
        elif choice3 == "blue":
            print("Game Over. You were eaten by beasts.")
        else:
            print("Game Over. You chose a door that doesn't exist.")
    else:
        print("Game Over. You got eaten by a trout.")
else:
    print("Game Over. You fell into a hole.")
