# exercise 3.11

import turtle

wn = turtle.Screen()
star = turtle.Turtle()
star.hideturtle()
star.pensize(3)

star.left(36)
for x in range(5):
    star.left(144)
    star.forward(70)

wn.mainloop()
