import pygame
import sys
import math

class road:
    def __init__(self, screen):
        self.screen = screen
        # Load road image
        self.road_image = pygame.image.load("CarRace/images/road.png")
        self.road_image = pygame.transform.scale(self.road_image, (800, 1200))  # Make it taller than the screen
        self.positionY = 0

    def move(self, speedY):
        self.positionY += speedY

    def draw(self):
           # Draw the road
        self.screen.blit(self.road_image, (0, -self.positionY ))
        self.screen.blit(self.road_image, (0, -self.positionY  + self.road_image.get_height())) 
