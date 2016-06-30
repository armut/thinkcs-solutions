import turtle
wn = turtle.Screen()

tess = turtle.Turtle()

background = input("Arkaplan rengini giriniz: ")
wn.bgcolor(background)

foreground = input("Tosbanın rengini giriniz: ")
tess.color(foreground)

pen_size = input("Kalem kalinligini giriniz: ")
tess.pensize(int(pen_size))

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()
