import turtle
import tkinter

len = 900
wid = 600

wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(len,wid)
wn.cv._rootwindow.resizable(False,False)

class draw_border(turtle.Turtle):
      def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.pu()
        self.color("red")
      def move(self):
        self.goto(-225,300)
        self.pd()
        self.rt(90)
        self.fd(600)


class post_button(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("grey")
        self.pu()
        self.goto(380,250)
        self.shapesize(3,5,outline=True)

class profile(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("black")
        self.pu()
        self.goto(-380,200)
        self.shapesize(3,3,outline=True)
        


class frame(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

        self.shape("square")
        self.color("black")
        self.pu()
        self.goto(180,-25)
        self.shapesize(24,23)
        self.dx = 0
        self.dy = 0
    def up(self):
        self.dy += 5
    def down(self):
        self.dy -= 5

postbutton = post_button()
Frame = frame()
Profile = profile()
drawborder = draw_border()


while True:
    wn.update()