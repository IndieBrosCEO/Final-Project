import pygame

pygame.init()
screen1 = 0
white = (255, 255, 255)
blue = (0, 0, 255)
xpos = 10
ypos = 10
screen = pygame.display.set_mode((1680, 970))
screen.fill(white)
pygame.mouse.set_visible(False)
while screen1 == 0:
    screen = pygame.display.set_mode((1680, 970))
    screen.fill(white)
    pygame.draw.circle(screen, blue, pygame.mouse.get_pos(), 10)
    pygame.display.update()
