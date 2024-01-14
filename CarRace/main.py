import pygame
import pygame.math
from Config import *

# PYGame Initialisieren
pygame.init()
screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)
clock = pygame.time.Clock()
dx = 0
speed = 4
# dy = 0
playerX = 400
playerY = 560
carHight = 68
carWith = 36


#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:  # Taste wurde gedrückt
            if event.key == pygame.K_RIGHT:
                dx = speed
            elif event.key == pygame.K_LEFT:
                dx = -1 * speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                dx = 0
            elif event.key == pygame.K_RIGHT:
                dx = 0
    screen.fill(GRAY)
    # draw the Player
    player = pygame.Rect((playerX - (carWith/2)), (playerY - (carHight/2)), carWith, carHight )
    image = pygame.image.load("images/car-top_view.png")
    image = pygame.transform.scale(image, (carWith, carHight))
    screen.blit(image, player)
    # move player
    playerX += dx
    pygame.display.update()
    clock.tick(60)


