import pandas

data_set = pandas.read_csv("nato_phonetic_alphabet.csv")

# using comprehension
data_dict = {row.letter: row.code for (index, row) in data_set.iterrows()}


def generate_phonetic():
    name = input("Enter your name: ").upper()
    try:
        final_list = [data_dict[letter] for letter in name]
    except KeyError:
        print('Sorry only alphabets allowed in the name')
        generate_phonetic()
    else:
        print(final_list)


generate_phonetic()
