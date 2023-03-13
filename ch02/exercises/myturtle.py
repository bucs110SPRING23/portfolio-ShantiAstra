import turtle
window = turtle.Screen()
Bob = turtle.Turtle()
Bob.color("purple")
Bob.shape("turtle")
for i in range(4):
    Bob.forward(50)
    Bob.right(90)
Bob.penup()
Bob.right(180)
Bob.forward(25)
Bob.pendown()
Bob.color("red")
for i in range(4):
    Bob.forward(25)
    Bob.left(90)
window.exitonclick()