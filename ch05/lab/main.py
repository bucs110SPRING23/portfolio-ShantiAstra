#imports
import pygame
def threenp1(n = 2):
    """ Conduct the 3n+1 sequence and return the number of iterations.
    3n+1 sequence is defined as:
    if number is even, divide it by 2
    if number is odd, multiply by three then add one
    repeat until the number becomes 0"""
    count = 0
    while n > 1.0:
        count += 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
    return count
def threenp1range(upper_limit = 2):
    """Finds the number of iterations of 3n+1 for each number from 2 to upper_limit
    and returns them as a dictionary"""
    objs_in_sequence = {}
    for i in range(0, upper_limit-1):
        objs_in_sequence[i+2]= threenp1(i+2)
    return objs_in_sequence
def graph_coordinates(objs_in_sequence):
    """Draws a point for each number and 3n+1 iterations in the dictionary
    using pygame, connects them with a line, and displays the max iterations."""
    x = 0
    y = 0
    max_so_far = 0
    font = None
    font_size = 30
    scale = 10
    dot_size = 2
    for num in objs_in_sequence:
        coord = (x, y)
        screen = pygame.display.get_surface()
        xpos = num 
        ypos = objs_in_sequence[num]
        if objs_in_sequence[num] > max_so_far:
            max_so_far = objs_in_sequence[num]
        pygame.draw.line(screen, "black", coord, (xpos,ypos))
        pygame.draw.circle(screen, "black", (xpos,ypos), dot_size)
        pygame.display.flip()
    new_display = pygame.transform.flip(screen, False, True)
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * scale, height * scale))
    font = pygame.font.Font(font, font_size)
    message = font.render("The maximum number of 3np1 iterations in this range is" + str(max_so_far), True, "black")
    pygame.display.flip()
    screen.blit(new_display, (0, 0))
    screen.blit(message, (10, 10))
    pygame.time.wait(5000)
def main():
    """Prints the sequence of 3n+1 iterations up to upper_limit
    then prints the dictionary from threenp1range which should say the same thing
    then makes a line graph in pygame to display the results"""
    upper_limit = int(input("How high would you like to check the 3n+1 iterations of?"))
    #start up pygame
    pygame.init()
    screen = pygame.display.set_mode()    
    screen.fill("green")
    pygame.display.flip()
    pygame.time.wait(500) 
    graph_coordinates(threenp1range(upper_limit))      
main()