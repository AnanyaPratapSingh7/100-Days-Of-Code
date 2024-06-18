import random

class Player:
    def __init__(self):
        self.cards = []
        self.total=0

    def addCard(self, card):
        self.cards.append(card)
        
        if card ==11:
            self.total += 1 if (self.total+11)>21 else 11
        else:
            self.total+=card

class Dealer:
    def __init__(self):
        self.deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]

    def deal(self, player):
        
        card = random.choice(self.deck)
        self.deck.remove(card)

        player.addCard(card)

    def result(self, player1, player2):
        print(f"Your final hand: {player1.cards}, final score: {player1.total}")
        print(f"Computer's final hand: {player2.cards}, final score: {player2.total}")

        if player1.total>21:
            print("You went over! You lose.")
        elif player2.total>21:
            print("Computer went over! You winnnn")
        elif 21-player1.total < 21-player2.total:
            print("You winnnnnnnnn!")
        elif 21-player1.total > 21-player2.total:
            print("You loseeee :(")
        else:
            print("It's a draw lol, what are the odds :P")