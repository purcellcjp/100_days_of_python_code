import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# import csv to daaframe
dtype_mapper = {'letter': 'string',
                'code': 'string'
                }
df = pd.read_csv('nato_phonetic_alphabet.csv', dtype=dtype_mapper)
# print(df.dtypes)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alphabet = {row.letter: row.code for (index, row) in df.iterrows()}
# print(alphabet['b'])

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():

    word = input('Enter a word: ').upper()
    try:
        mnemonic = [alphabet[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please')
        generate_phonetic()
    else:
        print(mnemonic)


generate_phonetic()
