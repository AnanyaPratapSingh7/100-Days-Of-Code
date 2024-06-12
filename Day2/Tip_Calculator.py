print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))

total = bill*(1 + tip/100)

persons = int(input("How many people to split the bill?5"))

print(f"Each person should pay: ${round(total/persons, 2)}")