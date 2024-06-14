from assets import *
import os
import random

game_over = False

while not game_over:
    
    selected_word = random.choice(words)
    answer=[]
    #Created empty answer
    for _ in selected_word:
        answer.append('_')

    lives = len(stages) - 1

    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        print(logo)

        print(stages[lives])

        if lives==0:
            print(f"You lost ! The correct word was: \t{selected_word}")
            break
        elif selected_word=="".join(answer):
            print("Congratulations ! You win ! ")
            break

        for letter in answer:
            print(letter , end="\t")

        print("\n")

        user_guess = input("Guess a letter : ")
        letter_found = False

        for i in range(0, len(selected_word)):
            if user_guess==selected_word[i]:
                answer[i]=selected_word[i]
                letter_found= True

        if not letter_found:
            lives-=1

    user_choice = input("Continue the game ? (Y/N) :\t")
    if not user_choice.lower()=='y':
        game_over=True
        print("Game Over")