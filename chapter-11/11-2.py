# exercise 11.2

import turtle

wn = turtle.Screen()
tess = turtle.Turtle()
alex = tess
alex.color("blue")

alex.forward(100)
tess.forward(-100)
wn.mainloop()

# Because alex and tess correspond to the same turtle,
# there is only one turtle, and hence, one color.
