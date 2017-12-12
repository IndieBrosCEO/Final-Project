import pygame
import sys
import pygame.mixer
import os
from pygame.locals import *

x = 400
y = 300

bkg = (255, 211, 0)
clr = (0, 0, 0)
squ = (8, 11, 134)

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)

current_path = os.path.dirname(__file__)
resource_path = os.path.join(current_path, 'resources')
image_path = os.path.join(resource_path, 'images')  #

pygame.init()
size = (1440, 1080)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetrahedron")
pygame.key.set_repeat(1, 1)
font = pygame.font.SysFont("Stencil", 20)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT]:
        x -= 5
    if keys_pressed[pygame.K_RIGHT]:
        x += 5
    if keys_pressed[pygame.K_UP]:
        y -= 5
    if keys_pressed[pygame.K_DOWN]:
        y += 5

    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > 1440:
        x = 1440
    if y > 1080:
        y = 1080

    screen.fill(bkg)
    text = font.render('(' + str(x) + ',' + str(y) + ')', True, clr)
    screen.blit(text, [10, 10])
    pygame.draw.rect(screen, squ, [x - 10, y - 10, 20, 20])
    pygame.display.flip()
    clock.tick(60)

    bullet = pygame.image.load(os.path.join('x.png'))
    bullets = []
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                bullets.append([event.pos[0] - 32, 500])

        mx, my = pygame.mouse.get_pos()

        for b in range(len(bullets)):
            bullets[b][0] -= 10
