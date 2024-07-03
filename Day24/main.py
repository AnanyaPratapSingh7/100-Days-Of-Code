
#Getting the list of names
with open("Input/Names/invited_names.txt") as names:
    name_list = names.read().split("\n")

with open("Input/Letters/starting_letter.txt") as file:
    sample_text = file.read()

for name in name_list:
    letter = sample_text.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(letter)        