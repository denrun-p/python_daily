"""Create a band name. """


def main():
    """Main method to generate band name. """
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
    cross = input("You're at a cross road. Where do you want to go? Type left or right:\n")  # noqa
    cross = cross.lower()
    if cross == "right":
        print("You fell into a hole. Game Over.")
        return
    elif cross != "left":
        print("That is not a valid direction. Game Over")
        return

    swim = input("You've come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim to swim across.\n").lower()  #noqa
    if swim == "swim":
        print("Attracked by a trout. Game Over.")
        return
    elif swim != "wait":
        print("That is not a valid option. Game Over.")
        return

    door = input("You've arrive at the island unharmed. There is a hourse with 3 doors. One red, one yellow, and one blue. Which color do you choose? \n").lower()  # noqa
    if door == "red":
        print("Burned by fire. Game Over.")
        return
    elif door == "blue":
        print("Eaten by beasts. Game Over.")
        return
    elif door != "yellow":
        print("That is not a door. Game Over.")
        return

    print("You Win!")
    print("")
    print('''
           ||====================================================================||
           ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
           ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
           ||\\$//        ~         '------========--------'                \\$//||
           ||<< /        /$\              // ____ \\                         \ >>||
           ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
           ||<<|        \\ //           || <||  >\  ||                        |>>||
           ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
        ||====================================================================||>||
        ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
        ||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
        ||\\$//        ~         '------========--------'                \\$//||\||
        ||<< /        /$\              // ____ \\                         \ >>||)||
        ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
        ||<<|        \\ //           || <||  >\  ||                        |>>||=||
        ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
        ||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
        ||>>|  12                     *\\/___\_//*   1989                  |<<||
        ||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
        ||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
        ||(100)===================  ONE HUNDRED DOLLARS =================(100)||
        ||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
        ||====================================================================||
    ''')

if __name__ == "__main__":
    main()
