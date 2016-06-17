# exercise 7.12

import turtle

wn = turtle.Screen()
turtl = turtle.Turtle()
turtl.pensize(3)

data = [(135,141), (-135,100), (135,71), (90,71), (45,100), (135,141),
        (-135,100), (-90,100)]

for (angle,step) in data:
    turtl.left(angle)
    turtl.forward(step)

wn.mainloop()
