import turtle
sides = int(input("How many sides would you like the turtle to draw?"))
side_length = float(input("How long should each side be?"))
internal_angle = 360/sides
window = turtle.Screen()
Emily = turtle.Turtle()
Emily.color("purple")
Emily.shape("turtle")
for i in range(sides):
    Emily.forward(side_length)
    Emily.left(internal_angle)
Emily.color("blue")
window.exitonclick()