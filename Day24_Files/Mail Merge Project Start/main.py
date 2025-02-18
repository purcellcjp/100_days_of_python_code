# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

OUTPUT_DIRECTORY = './Output/ReadyToSend/'


# get template letter
with open('./Input/Letters/starting_letter.txt') as file:
    template = file.read()
# print(template)

# print('-'*20)

# get list of names
with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()

# loop through names to create new file
for name in names:
    new_letter = template
    # replace [name] with name
    invite = new_letter.replace('[name]', name.strip())
    new_file = f'{OUTPUT_DIRECTORY}letter_for_{name.strip()}.txt'
    print(new_file)
    print('-'*20)
    with open(new_file, mode='w') as file:
        file.write(invite)
