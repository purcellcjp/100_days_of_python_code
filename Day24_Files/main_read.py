file_name = 'my_file.txt'

# file = open(file_name)
# text = file.read()
# print(text)
# file.close()

# preferred method


def read_example():
    with open(file_name) as file:
        text = file.read()
        print(text)


def write_example():
    with open(file_name, mode='w') as file:
        file.write('new text')


def append_example():
    with open(file_name, mode='a') as file:
        file.write('\nsome new text\n')


def write_new_file():
    # only creates new file in write mode
    with open('new_file.txt', mode='w') as file:
        file.write('new text.')


def test_desktop():
    with open('/Users/purce/Desktop/new_file.txt') as file:
        text = file.read()
    print(text)

# write_example()
# append_example()
# read_example()
# write_new_file()
test_desktop()
