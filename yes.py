import sys
import pygame.mixer
import os
import random

x = 400
y = 300

bulletlife = 0
bulletlifecountd = 0

bkg = (255, 211, 0)
clr = (0, 0, 0)
squ = (8, 11, 134)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

current_path = os.path.dirname(__file__)
resource_path = os.path.join(current_path, 'resources')
image_path = os.path.join(resource_path, 'images') #

pygame.init()
size = (720, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetrahedron")
pygame.key.set_repeat(1, 1)
font = pygame.font.SysFont("Stencil", 20)
clock = pygame.time.Clock()
pygame.mouse.set_visible(True)

bx = 100
by = 100

screen.fill(bkg)
pygame.display.update()
while True:
    pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_a]:
        x -= 5
    if keys_pressed[pygame.K_d]:
        x += 5
    if keys_pressed[pygame.K_w]:
        y -= 5
    if keys_pressed[pygame.K_s]:
        y += 5

    else:
        bx = x
        by = y
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > 720:
        x = 720
    if y > 720:
        y = 720

    if pygame.mouse.get_pressed()[0] == 1:
            bulletlife = 0
            bulletlifecountd = 0
            pygame.draw.circle(screen, red, (int(round(bx)), int(round(by))), 10)
            pygame.display.update()
            bx = x
            by = y

            while bulletlife == 0:

                if pygame.mouse.get_pos()[0] < x + 25:
                    bx = bx - 1
                if pygame.mouse.get_pos()[1] < y + 25:
                    by = by - 1
                if pygame.mouse.get_pos()[0] > x - 25:
                    bx = bx + 1
                if pygame.mouse.get_pos()[1] > y - 25:
                    by = by + 1
                if bulletlifecountd == 100 or bulletlifecountd > 100:
                    bulletlife = 1
                pygame.draw.circle(screen, red, (int(round(bx)), int(round(by))), 10)
                pygame.display.update()
                bulletlifecountd += 1

    def enemies_killed(count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Score: " + str(count), True, black)
        gameDisplay.blit(text, (0, 0))

    screen.fill(bkg)
    text = font.render('(' + str(x) + ',' + str(y) + ')', True, clr)
    screen.blit(text, [10, 10])
    pygame.draw.rect(screen, squ, [x - 10, y - 10, 20, 20])
    pygame.display.flip()
    clock.tick(60)

