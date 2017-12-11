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
x = 0
y = 0

while screen1 == 0:
    screen = pygame.display.set_mode((1680, 970))
    screen.fill(white)
    pygame.draw.circle(screen, blue, (x, y), 10)
    if pygame.KEYDOWN(unicode) == pygame.K_w:
        y += 5
    if pygame.KEYDOWN[pygame.K_s]:
        y -= 5
    pygame.display.update()
