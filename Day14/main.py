from game_data import data
from art import logo, vs
import os
import random

game_on = True

score = 0

choiceA = random.choice(data)
choiceB = random.choice(data)

os.system('cls' if os.name=='nt' else 'clear')
print(logo)

while game_on:

    print(f"Compare A: {choiceA['name']}, a {choiceA['description']}, from {choiceA['country']}.")
    print(vs)
    print(f"Against B: {choiceB['name']}, a {choiceB['description']}, from {choiceB['country']}.")

    user_choice = input("Who has more followers? Type 'A' or 'B':\t")

    winner = choiceA if choiceA['follower_count']>choiceB['follower_count'] else choiceB

    selected = choiceA if user_choice=='A' else choiceB

    os.system('cls' if os.name=='nt' else 'clear')
    print(logo)

    if selected==winner:
        score+=1
        print(f"You're right! Current score: {score}.")
        choiceA = winner
        choiceB = random.choice(data)

        while choiceB==choiceA:
            choiceB = random.choice(data)
    else:
        game_on = False
        print(f"Sorry, that's wrong. Final score: {score}")