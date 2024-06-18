############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import os
from brain import Player, Dealer

logo =" B L A C K J A C K "

game_on = True

while game_on:
    
    #Checking whether to continue the game
    check = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if check=='n':
        game_on= False
        break
    
    #CLearing screen and displaying logo
    os.system('cls' if os.name=='nt' else 'clear')
    print(logo)

    #Crearing Players
    user = Player()
    comp = Player()

    dealer = Dealer()

    round_start = True
    #Dealing two cards Each
    dealer.deal(user)
    dealer.deal(comp)

    dealer.deal(user)
    dealer.deal(comp)

    while True:
        print(f"Your cards: {user.cards}, current score: {user.total}")
        print(f"Computer's first card: {comp.cards[0]}")

        more_cards = input("Type 'y' to get another card, type 'n' to pass: ")

        if more_cards=='n':
            break

        dealer.deal(user)
        
        if user.total>21:
            dealer.result(user, comp)
            round_start= False
            break
        
        if comp.total<17:
            dealer.deal(comp)
        
        if comp.total>21:
            dealer.result(user, comp)
            round_start=False
            break

        

    while comp.total<17:
        dealer.deal(comp)

    if round_start:
        dealer.result(user, comp)