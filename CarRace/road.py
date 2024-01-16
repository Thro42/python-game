#road.py
import pygame
import sys

class Road:
    def __init__(self, screen):
        self.screen = screen
        self.road_image = pygame.image.load("CarRace/images/road.png")
        self.road_image = pygame.transform.scale(self.road_image, (800, 1200))
        self.image_height = self.road_image.get_height()
        self.positionY = 0

    def move(self, speedY):
        self.positionY += speedY
        if self.positionY > self.image_height:
            self.positionY -= self.image_height
        if self.positionY < -self.image_height:
            self.positionY += self.image_height

    def draw(self):
        # Draw the Road in a loop
        self.screen.blit(self.road_image, (0, -self.positionY))
        self.screen.blit(self.road_image, (0, -self.positionY - self.image_height))

