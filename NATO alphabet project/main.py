import pandas as pd


data = pd.read_csv('nato_phonetic_alphabet.csv')

nato_data = {row.letter:row.code for (index,row) in data.iterrows()}
#
# on = True
# while on:
input_text = str(input("Enter a text: ")).upper()

try:
    result = [nato_data[w] for w in input_text]
except KeyError:
    print("sorry only enter alphabets")
else:
    print(result)
finally:
    input_text = str(input("Enter a text: ")).upper()



