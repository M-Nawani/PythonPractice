import pandas

data_set = pandas.read_csv("nato_phonetic_alphabet.csv")

# using comprehension
data_dict = {row.letter: row.code for (index, row) in data_set.iterrows()}

name = input("Enter your name: ").upper()
final_list = [data_dict[letter] for letter in name]
print(final_list)



