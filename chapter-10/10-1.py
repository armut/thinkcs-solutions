# exercise 10.1
import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def h1():
    tess.forward(30)

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def h4():
    wn.bye()

def make_red():
    tess.color("red")

def make_green():
    tess.color("green")

def make_blue():
    tess.color("blue")

pen_size = 1
def increase_penwidth():
    global pen_size
    if pen_size <= 20:
        pen_size += 1
    tess.pensize(pen_size)

def decrease_penwidth():
    global pen_size
    if pen_size >= 1:
        pen_size -= 1
    tess.pensize(pen_size)

def change_title():
    wn.title("Tess is now in " + str(tess.color()))


wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

wn.onkey(make_red, "r")
wn.onkey(make_green, "g")
wn.onkey(make_blue, "b")

wn.onkey(increase_penwidth, "plus")
wn.onkey(decrease_penwidth, "minus")

wn.onkey(change_title, "t")

wn.listen()
wn.mainloop()
