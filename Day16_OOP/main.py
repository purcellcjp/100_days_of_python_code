import os
# from turtle import Turtle, Screen

# os.system('cls')

# myTurtle = Turtle()
# # print(myTurtle)
# myTurtle.shape('turtle')
# myTurtle.color('red','green')
# myTurtle.forward(100)
# myTurtle.left(120)
# myTurtle.forward(100)

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         myTurtle.color(c)
#         myTurtle.forward(steps)
#         myTurtle.right(30)
        

# myScreen = Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()

from prettytable import PrettyTable

x = PrettyTable() 
x.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"]) 
x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386]) 
x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769]) 
x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])
x.align = 'l'

x.align['Annual Rainfall'] = 'r'

print(x)
