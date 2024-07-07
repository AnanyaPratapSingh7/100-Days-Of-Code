import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (idx, row) in data.iterrows()}

valid_word_entered = False

while not valid_word_entered:

    user_input = input("Enter a word : ")

    try:
        result = [nato_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters of the alphabet are allowed")
    else:
        valid_word_entered = True

print(result)