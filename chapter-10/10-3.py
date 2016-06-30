# exercise 10.3
import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Turtles becomes a traffic light!")
wn.bgcolor("lightgreen")
green = turtle.Turtle()
red = turtle.Turtle()
orange = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    green.pensize(3)
    green.color("black", "darkgrey")
    green.begin_fill()
    green.forward(80)
    green.left(90)
    green.forward(200)
    green.circle(40, 180)
    green.forward(200)
    green.left(90)
    green.end_fill()

draw_housing()

green.penup()
green.forward(40)
green.left(90)
green.forward(50)
green.shape("circle")
green.shapesize(3)
green.fillcolor("green")

orange.hideturtle()
orange.penup()
orange.forward(40)
orange.left(90)
orange.forward(120)
orange.shape("circle")
orange.shapesize(3)
orange.fillcolor("orange")

red.hideturtle()
red.penup()
red.forward(40)
red.left(90)
red.forward(190)
red.shape("circle")
red.shapesize(3)
red.fillcolor("red")

state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:
        orange.showturtle()
        green.hideturtle()
        state_num = 1
    elif state_num == 1:
        red.showturtle()
        orange.hideturtle()
        state_num = 2
    else:
        green.showturtle()
        red.hideturtle()
        state_num = 0

    wn.ontimer(advance_state_machine, 500)

# Bind the event handler to the space key
advance_state_machine()
wn.listen()
wn.mainloop()
