print("Welcome to the Treasure Island!\nYour mission is to find the treasure.")
user_choice=input(("You are on a crossroad. Where do you want to go? Type 'left' or 'right' : "))
if user_choice!='left':
    print("Fall into a hole. Game Over.")
else:
    user_choice = input("You arrive at a Lake. Type 'swim' or 'wait' : ")
    if(user_choice!="wait"):
        print("Attack by a trout. Game Over.")
    else:
        user_choice = input("You arrive at a door. Type 'Red','Blue' or 'Yellow': ")
        if user_choice=='Red':
            print("Burnt by fire. Game Over.")
        elif user_choice=='Yellow':
            print("Eaten by beasts. Game Over.")
        elif user_choice=='Blue':
            print("You Win!")
        else:
            print("Game Over")