import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
def winner(race):
    l_distance = leonardo.xcor()
    m_distance = michelangelo.xcor()
    if l_distance > m_distance:
        print("Leonardo the blue turtle has won the", race, "race")
    elif m_distance > l_distance:
        print("Michelangelo the orange turtle has won the", race, "race")
    else:
        print("The", race, "race is a draw")  
    michelangelo.goto(-100,20)
    leonardo.goto(-100,-20)

# Race 1
m_speed = random.randrange(1,101)
l_speed = random.randrange(1,101)
michelangelo.forward(m_speed)
leonardo.forward(l_speed)
winner("first")

# Race 2
for i in range(10):
    m_speed = random.randrange(1,11)
    l_speed = random.randrange(1,11)
    michelangelo.forward(m_speed)
    leonardo.forward(l_speed)
winner("second")
window.exitonclick()

# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()
window.fill("aliceblue")
points = []
num_sides = [3, 4, 6, 20, 100, 360]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
side_length = 250
xpos = 650
ypos = 400

for shape in range(len(num_sides)):
    for i in range(num_sides[shape]):
        angle = 360/num_sides[shape]
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x,y])
    pygame.draw.polygon(window, colors[shape], points)
    pygame.display.flip()
    pygame.time.wait(1000)
    window.fill("aliceblue")
    pygame.display.flip()
    points = []
    pygame.time.wait(500)

