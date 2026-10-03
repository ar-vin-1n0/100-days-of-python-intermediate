import pandas as pd


data = pd.read_csv('nato_phonetic_alphabet.csv')

nato_data = {row.letter:row.code for (index,row) in data.iterrows()}

input_text = str(input("Enter a text: ")).upper()

result = [nato_data[w] for w in input_text if w in nato_data]

print(result)


