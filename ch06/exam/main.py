import turtle
import random
def setup_turtle(name, color = "black", xpos = 0, ypos = 0):
    """Put the turtle in the right color in the right position ready to draw a shape.
    This is code that needs to be called every time there is a new turtle, so it is in its own function."""
    name.hideturtle()
    name.shape("turtle")   
    name.color(color)
    name.penup()
    name.goto(xpos,ypos)
    name.pendown()
    name.showturtle()
    name.begin_fill()

def place_check(name, old_positions):
    """Check the current position of the turtle.
    If any of its coordinates are more extreme than the currently saved ones,
    overwrite them with the new highest or lowest coordinate"""
    xmax = old_positions[0]
    ymax = old_positions[1]
    xmin = old_positions[2]
    ymin = old_positions[3]
    x, y = name.pos()
    if x > xmax:
        xmax = x
    elif x < xmin:
        xmin = x
    if y > ymax:
        ymax = y
    elif y < ymin:
        ymin = y
    positions = (xmax, ymax, xmin, ymin)
    return positions

def draw_star(xpos = 0, ypos = 0, size = 5):
    """Draw a star at a position determined by the parameters
    and of a size determined by the parameters using a turtle named stella.
    Fill the star with pale yellow, then hide the turtle. Keep track of 
    and return the max and min x and y values that the turtle travels over.
    These values will be used for checking possible overlaps for new, randomly generated star locations"""
    star_color = (255,255,204)
    internal_angle = 70
    external_angle = 160
    num_points = 4
    #this tuple tracks the maximum and minimum x and y values experienced by the turtle and will be updated through place_check
    positions = (xpos, ypos, xpos, ypos)
    stella = turtle.Turtle()
    setup_turtle(stella, star_color, xpos, ypos)
    stella.left(170)
    for _ in range(num_points):
        stella.forward(size)
        stella.right(internal_angle)
        stella.forward(size)
        stella.left(external_angle)
        positions = place_check(stella, positions)      
    stella.end_fill()
    stella.hideturtle()
    return positions

def draw_sun(xpos = 0, ypos = 0):
    """Draw the sun at a position determined by the parameters
    using a turtle named apollo, after the sun god.
    Fill the sun with an orangey-yellow color, then hide the turtle. Note that 
    apollo moves faster than the other turtles because he has more drawing to do. 
    Keep track of and return the max and min x and y values that the turtle travels over"""
    sun_color = (255, 212, 51)
    size = 75
    angle = 170
    #this tuple tracks the maximum and minimum x and y values experienced by the turtle
    positions = (xpos, ypos, xpos, ypos)
    apollo = turtle.Turtle()
    apollo.speed(8)
    setup_turtle(apollo, sun_color, xpos, ypos)
    for _ in range(18):
        apollo.forward(size)
        apollo.right(angle)
        positions = place_check(apollo, positions)
    apollo.end_fill()
    apollo.hideturtle()
    return positions

def draw_moon(xpos = 0, ypos = 0):
    """Draw the moon at a position determined by the parameters
    using a turtle named luna. Fill the moon with light greyish blue, then hide the turtle. 
    Keep track of and return the max and min x and y values that the turtle travels over"""  
    inner_size = 3
    outer_size = 4
    num_segments = 35
    inner_angle = 3
    outer_angle = 5
    tip_angle = 150
    moon_color = (220, 231, 236)
    #this tuple tracks the maximum and minimum x and y values experienced by the turtle
    positions = (xpos, ypos, xpos, ypos)
    luna = turtle.Turtle()
    setup_turtle(luna, moon_color, xpos, ypos)
    for _ in range(num_segments):
        luna.forward(inner_size)
        luna.left(inner_angle)
        positions = place_check(luna, positions)
    luna.right(tip_angle)
    for _ in range(num_segments):
        luna.forward(outer_size)
        luna.right(outer_angle)
        positions = place_check(luna, positions)
    luna.end_fill()
    luna.hideturtle()
    return positions

def main():
    sky_color = (102,55,255)
    sunpos = (-150, 150)
    moonpos = (150, -150)
    # this list tracks the tuples that describe squares of the screen that are already occupied with drawings
    locations = []
    star_num = int(input("How many stars should the turtles draw?"))
    max_stars = 50
    window = turtle.Screen()
    width = 500
    height = 500
    window.screensize(width, height)
    window.colormode(255) 
    window.bgcolor(sky_color)
    draw_sun(width/2, height/2)
    locations.append(draw_sun(sunpos[0], sunpos[1]))
    locations.append(draw_moon(moonpos[0], moonpos[1]))
    # prevents an infinite loop due to too many stars and no free spaces
    if star_num > max_stars:
        star_num = max_stars
    for _ in range(star_num):
        star_not_drawn = True
        while star_not_drawn:
            size = random.randint(2, 15)
            xpos = random.randint(-width/2 + size*2, width/2)
            ypos = random.randint(-height/2 + size, height/2 - size)
            no_overlaps_yet = True
            for tuple in locations:
                if tuple[2] < xpos and xpos - size * 2 < tuple[0] and tuple[3] < ypos + size and ypos - size < tuple[1]:
                    no_overlaps_yet = False
                else:
                    no_overlaps_yet = True
            if no_overlaps_yet:
                locations.append(draw_star(xpos, ypos, size))
                star_not_drawn = False
    window.exitonclick()
main()
