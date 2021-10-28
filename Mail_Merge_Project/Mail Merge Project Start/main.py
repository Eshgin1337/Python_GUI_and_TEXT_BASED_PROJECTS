PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_data:
    names = name_data.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names:
        new_letter = letter_contents.replace(PLACE_HOLDER, name.strip())
        with open(f"Output/ReadyToSend/letter_to_{name.strip()}.txt", "w") as birthday_invitation:
            birthday_invitation.write(new_letter)

