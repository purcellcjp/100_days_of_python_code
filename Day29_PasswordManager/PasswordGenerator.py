import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

new_password = ''
hard_password = ''

# loop through number of requested letters
if nr_letters > 0:
    for x in range(0, nr_letters):
        new_password += random.choice(letters)
if nr_numbers > 0:
    for x in range(0, nr_numbers):
        new_password += random.choice(numbers)

if nr_symbols > 0:
    for x in range(0, nr_symbols):
        new_password += random.choice(symbols)

# Sramble the results
# tot_chars = nr_letters + nr_symbols + nr_numbers
# for x in range(0, tot_chars):
#     hard_password += random.choice(new_password)

# Hard method
chars=[]
if nr_letters > 0:
    for x in range(0, nr_letters):
        chars.append(random.choice(letters))

if nr_numbers > 0:
    for x in range(0, nr_numbers):
        chars.append(random.choice(numbers))

if nr_symbols > 0:
    for x in range(0, nr_symbols):
        chars.append(random.choice(symbols))

random.shuffle(chars)
for char in chars:
    hard_password += char


print(new_password)
print(chars)
print(hard_password)