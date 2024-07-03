import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (idx, row) in data.iterrows()}

user_input = input("Enter a word : ")

result = [nato_dict[letter.upper()] for letter in user_input]

print(result)