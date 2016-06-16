# exercise 7.11

import turtle

wn = turtle.Screen()
pirate = turtle.Turtle()
pirate.shape("turtle")

data = [(160,20), (-43,10), (270,8), (-43,12)]
for (turn,step) in data:
    pirate.left(turn)
    pirate.forward(step)

wn.mainloop()
