import os

logo="""                
               (_()  
          \__/  ||   \ \__/
          (oo)  /)    \(oo)
         //~~\\//       //~~\\
         \\__/\/   _____\\__//_____
          |/\|    |                |
    _____ |||| ___|                |______
   ______(_)(_)___|________________|____"""


more_bidders = True
bidders = {}

highest_bid=0
highest_bidder=""

while more_bidders:
    os.system('cls' if os.name=='nt' else 'clear')
    print("Welcome to the Silent Auction ! ")
    print(logo)
    print("\n\n")
    name = input("What is your name :\t")
    bid = int(input("What's your bid :\t"))

    bidders.update({name:bid})

    if bid>highest_bid:
        highest_bid = bid
        highest_bidder= name

    more_bidders = input("More bidders ? 'Yes' or 'No :\t'")=='Yes'

os.system('cls' if os.name=='nt' else 'clear')
print("Welcome to the Silent Auction ! ")
print(logo)
print("\n\n")
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")