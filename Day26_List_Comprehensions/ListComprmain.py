import os
os.system('cls')

# List comprehensions
numbers = [1, 2, 3, 4, 5]
new_list = [n + 1 for n in numbers]
print(new_list)

print('-'*20)

# list comprehensions also work with strings
name = 'Christopher'
letters_list = [letter for letter in name]
print(letters_list)

# list comprehension with range
print('-'*20)
doubled_num_list = [n*2 for n in range(1, 5)]
print(doubled_num_list)

print('-'*20)

# List comprehension with conditions
# Create new list of names with 4 characters or less
names = ['Alex', 'Christopher', 'Dave', 'Eleanor', 'Beth', 'Matthew']
short_names = [name for name in names if len(name) < 5]
print(short_names)
print('-'*20)
# convert names greater than 4 to upper case
upper_names = [name.upper() for name in names if len(name) > 4]
print(upper_names)
print('-'*20)

# example from udemy challenge
'''
with open('file1.txt') as file1:
    lines1 = [line.strip() for line in file1]
# print(lines1)

with open('file2.txt') as file2:
    lines2 = [line.strip() for line in file2]
# print(lines2)

result =[n for n in lines1 if n in lines2]


print(result)
'''