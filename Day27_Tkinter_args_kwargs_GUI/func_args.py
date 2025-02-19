# *args example - takes unlimited number of parameters
# the parameters are also positional: args[0] returns first parameter value
def add(*args):
    tot = 0
    for n in args:
        tot += n
    return tot

# print(add(1,2,3,4,89))


# **kwargs holds parameters in a dictionary
#
def my_example(**kwargs):
    for key, value in kwargs.items():
        print(key, value, sep='|')

# my_example(add=5, multiply=2)


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
# calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        # use get() method in case attribute is not present
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')


my_car = Car(make='Honda', model='Odyssey')
print(my_car.model)
