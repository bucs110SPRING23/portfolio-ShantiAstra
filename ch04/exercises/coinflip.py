import turtle
import random
window = turtle.Screen()
steve = turtle.Turtle()
steve.color("purple")
steve.shape("turtle")
dimensions = turtle.screensize()
width = dimensions[0]
height = dimensions[1]
steve.goto(0,0)
def walk():
    if random.randint(0,1) == 1:
        steve.right(90)
    else:
        steve.left(90)
    steve.forward(50)
while -width < steve.xcor() < width and -height < steve.ycor() < height:
    walk()

window.exitonclick()