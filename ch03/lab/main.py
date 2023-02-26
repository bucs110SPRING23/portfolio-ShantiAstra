# import required modules
import pygame
import random
import math

# Define basic variables - note that a player color cannot be green or red
board_color = "orange"
background_color = (0,75, 180)
player1_score = 0
player1_color = "yellow"
player2_score = 0
player2_color = "purple"
time_delay = 500
dart_size = 10
dart_color_dot = 3
line_color = "black"
darts_per_player = 10

# pygame based variables
pygame.init()
screen = pygame.display.set_mode()
screen_size = pygame.display.get_window_size()
screen_width = float(screen_size[0])
screen_height = float(screen_size[1])
if screen_width <= screen_height:
    smaller_dimension = screen_width
else:
    smaller_dimension = screen_height
width_border = (screen_width-smaller_dimension)/2
height_border = (screen_height-smaller_dimension)/2

# function that throws a dart and draws the result
def throw_a_dart(player_color):
    x = random.randrange(screen_width)
    y = random.randrange(screen_height)
    distance_from_center = math.hypot(x-(screen_width/2), y-(screen_height/2))
    is_in_circle = distance_from_center <= smaller_dimension/2
    if is_in_circle == True:
        dart_color = "green"
        add_score = True
    else:
        dart_color = "red"
        add_score = False
    pygame.draw.circle(screen, dart_color, [x,y], dart_size)
    pygame.draw.circle(screen, player_color, [x,y], dart_color_dot)
    pygame.display.flip()
    pygame.time.wait(time_delay)
    return add_score


# Draw dartboard
screen.fill(background_color)
pygame.draw.circle(screen, board_color, [screen_width/2, screen_height/2], smaller_dimension/2)
pygame.draw.line(screen, line_color, (width_border, screen_height/2), (screen_width - width_border, screen_height/2))
pygame.draw.line(screen, line_color, (screen_width/2, height_border), (screen_width/2, screen_height-height_border))
pygame.display.flip()
pygame.time.wait(time_delay)

# play game of darts and print results
for _ in range(darts_per_player):
    if throw_a_dart(player1_color):
        player1_score = player1_score +1
    if throw_a_dart(player2_color):
        player2_score = player2_score +1
if player1_score > player2_score:
    print("Player 1 using the", player1_color, "darts has won this round of darts")
elif player1_score < player2_score:
    print("Player 2 using the", player2_color, "darts has won this round of darts")
else:
    print("This round of darts was a draw. Please play again")
    
