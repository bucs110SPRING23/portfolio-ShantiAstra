import turtle
def draw_eq_shape(turtle, num_sides, side_length):
    internal_angle = 360/num_sides
    for _ in range(num_sides):
        turtle.forward(side_length)
        turtle.right(internal_angle)
    

mike = turtle.Turtle()
mike.color("green")
mike.shape("turtle")
num_sides = int(input("How many sides should the shape this turtle draws have?"))
side_length = int(input("How long should each side be?"))
window = turtle.Screen()
draw_eq_shape(mike, num_sides, side_length)
window.exitonclick()