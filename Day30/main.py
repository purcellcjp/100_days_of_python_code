# Error Handling

# FileNotFound
# try:
#     file = open('bogus_file.txt')
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['key'])

# except FileNotFoundError:
#     file = open('bogus_file.txt', 'w')
#     file.write('something')
# except KeyError as err_msg:
#     print(f'The key {err_msg} does not exist.')
# else:
#     content = file.read()
#     print(content)
# finally:
#     # runs no matter what
#     #not often used
#     file.close()
#     print('file closed')
#     raise TypeError('made up')

# Raise Exceptions

height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('Human height should not exceed 3 meters')

if weight > 300:
    raise ValueError('Human weight should not exceed 300 KG.')

bmi = weight/height **2

print(f'BMI: {bmi}')
