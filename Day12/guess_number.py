import random
import os

NUMBER = random.randint(1,101)

def start_game():
    os.system('cls' if os.name=='nt' else 'clear')
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking a of a number between 1 and 100.")
    






def main():

    start_game()

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


    atempts_left = 5 if difficulty=='hard' else 10

    game_on = True
    while game_on:    
        if atempts_left==0:
            print(f"You have run out of guesses, you lose. The number was {NUMBER}")
            game_on= False
            break

        print(f"You have {atempts_left} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess>NUMBER:
            print("Too high.\nGuess Again.")
        elif user_guess<NUMBER:
            print("Too low.\nGuess Again.")
        else:
            print(f"You guessed it correct! You still had {atempts_left} attempts left!")
            game_on= False
            break

        atempts_left-=1    

main()