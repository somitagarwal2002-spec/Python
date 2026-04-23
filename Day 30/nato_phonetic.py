import pandas as pd 

data = pd.read_csv("Day 26/nato_phonetic_alphabet.csv")

dictionary = {row.letter:row.code for (index, row) in data.iterrows()}
print(dictionary)

def generate_phonetic_word():
    name = input("Enter a word: ").upper().strip()  
    try:     
        code_list = [dictionary[new_item] for new_item in name]
    except KeyError:
        print("Sorry! only letters in the alphabet please")
        generate_phonetic_word()
    else:
        print(code_list)

generate_phonetic_word()
