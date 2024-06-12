import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissors]

user_input = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors."))

user_choice = choice[user_input]
computer_choice = random.choice(choice)

print(f"Your choice : \n{user_choice}\nComputer choice : \n{computer_choice}\n")

if user_choice==rock:
    if computer_choice==rock:
        print("It is a draw.")
    elif computer_choice==paper:
        print("You lose.")
    else:
        print("You Win!")
elif user_choice==paper:
    if computer_choice==rock:
        print("You Win!")
    elif computer_choice==paper:
        print("It is a draw.")
    else:
        print("You lose.")
else:
    if computer_choice==rock:
        print("You lose.")
    elif computer_choice==paper:
        print("You Win!")
    else:
        print("It is a draw.")