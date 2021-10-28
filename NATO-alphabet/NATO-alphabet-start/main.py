import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_word_pairs = {row.letter: row.code for (index, row) in data.iterrows()}

is_inappropriate = True
while is_inappropriate:
    user_input = input().upper()
    try:
        nato_list = [letter_word_pairs[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
    else:
        print(nato_list)
        is_inappropriate = False
