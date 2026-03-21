import pandas as pd 

data = pd.read_csv("Day 26/nato_phonetic_alphabet.csv")

dictionary = {row.letter:row.code for (index, row) in data.iterrows()}
# print(dictionary)

name = input("Enter a word: ").upper().strip()
code_list = [dictionary[new_item] for new_item in name]

print(code_list)
