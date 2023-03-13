# import required modules
import pygame
import random
import math

# Define basic variables - note that a player color cannot be green or red
board_color = "orange"
background_color = (0,75, 180)
player1_color = "yellow"
player2_color = "purple"
time_delay = 500
long_delay = 5000
dart_size = 10
dart_color_dot = 3
line_color = "black"
darts_per_player = 10
bet_not_done = True

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
font = pygame.font.Font(None,30)
bet_player1 = pygame.Rect(0,0, 200, 100)
bet_player2 = pygame.Rect(screen_width - 200,0, 200, 100)

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

# function that plays a game of darts and prints results onscreen
def game_of_darts():
    player1_score = 0
    player2_score = 0
    for _ in range(darts_per_player):
        if throw_a_dart(player1_color):
            player1_score +=1
        if throw_a_dart(player2_color):
            player2_score +=1
    if player1_score > player2_score:
        winner = "player1"
        message = "Player 1 has won this round of darts using the " +  str(player1_color) + " darts with a final score of " + str(player1_score)
    elif player1_score < player2_score:
        winner = "player2"
        message = "Player 2 has won this round of darts using the " + str(player2_color) + " darts with a final score of "+ str(player2_score)
    else:
        message = "This round of darts was a draw. Both players had a final score of" + str(player1_score)
    text = font.render(message, True, "white")
    text_rect = text.get_rect(center = (screen_width/2, screen_height -75))
    screen.blit(text, text_rect)
    if bet == winner:
        text = font.render("You bet correctly", True, "white")
        text_rect = text.get_rect(center = (screen_width/2, screen_height -25))
        screen.blit(text, text_rect)
    else:
        text = font.render("Too bad, try again next time", True, "white")
        text_rect = text.get_rect(center = (screen_width/2, screen_height -25))
        screen.blit(text, text_rect)
    
    pygame.display.flip()
    pygame.time.wait(long_delay)
    
# function to draw dartboard and betting buttons
def draw_board():
    screen.fill(background_color)
    pygame.draw.circle(screen, board_color, [screen_width/2, screen_height/2], smaller_dimension/2)
    pygame.draw.line(screen, line_color, (width_border, screen_height/2), (screen_width - width_border, screen_height/2))
    pygame.draw.line(screen, line_color, (screen_width/2, height_border), (screen_width/2, screen_height-height_border))
    pygame.draw.rect(screen, player1_color, bet_player1)
    pygame.draw.rect(screen, player2_color, bet_player2)
    text = font.render("Bet on Player 1", True, "black")
    screen.blit(text, (10, 40))
    text = font.render("Bet on Player 2", True, "black")
    screen.blit(text, (screen_width - 190, 40))
    pygame.display.flip()

# Mainloop
while bet_not_done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bet_player1.collidepoint(event.pos):
                bet_not_done = False
                bet = "player1"
            elif bet_player2.collidepoint(event.pos):
                bet_not_done = False
                bet = "player2"
    draw_board()
game_of_darts()
