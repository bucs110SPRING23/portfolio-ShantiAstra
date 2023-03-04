import pygame
originX = 50
originY = 500
def threenp1(n):
    count = 0
    while n > 1.0:
       count += 1
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return count
def threenp1range(upper_limit):
    objs_in_sequence = {}
    for i in range(upper_limit-1):
       objs_in_sequence[i+2]= threenp1(i+2)
    return objs_in_sequence
def main(upper_limit):
    for i in range(upper_limit-1):
      print(threenp1(i+2))
    print(threenp1range(upper_limit))
    line_graph(threenp1range(upper_limit))
    screen.fill("green")
    pygame.draw.line(screen, "black", (originX, 0), (originX, 1500))
    pygame.draw.line(screen, "black", (0, originY), (1500, originY))
    pygame.display.flip()
    pygame.time.wait(5000)
def line_graph(objs_in_sequence):
    x = originX
    y = originY
    for num in objs_in_sequence:
       coord = (x, y)
       x = originX + num
       y = originY - objs_in_sequence[num]
       #pygame.draw.line(screen, "black", coord, (x,y))
       pygame.draw.circle(screen, "black", (x,y), 5)
pygame.init()
screen = pygame.display.set_mode()        
main(4)