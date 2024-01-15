import pygame
import sys
import math

class Player:
    def __init__(self, screen, posX, posY):
        self.screen = screen
        self.speed = 0
        self.velocity = 0.05
        self.positionX = posX
        self.positionY = posY
        self.carHeight = 68
        self.carWidth = 36
        # Load car image
        self.car_image = pygame.image.load("CarRace/images/car-top_view.png")
        self.car_image = pygame.transform.scale(self.car_image, (self.carWidth, self.carHeight))
        self.rotation_angle = 0
        self.rotation_speed = 1
        self.maxX = 800
        self.maxY = 600

    def rotate(self,direction):
        if (direction  != 0):
            self.rotation_angle += self.rotation_speed * direction

    def speed_up(self):
        self.speed += self.velocity
    def break_up(self):
        self.speed -= self.velocity * 3
        if self.speed < 0:
            self.speed = 0
    def drive(self):
        self.speed -= self.velocity/3
        if self.speed < 0:
            self.speed = 0

    def move(self):
        # Update velocity components based on the angle
        dx = -math.sin(math.radians(self.rotation_angle)) * self.speed
        dy = -math.cos(math.radians(self.rotation_angle)) * self.speed  # Negative due to inverted Y-axis
        # Update player position
        self.positionX += dx
        self.positionY += dy
        if self.positionX < 0:
            self.positionX = 0
        if self.positionY < 0:
            self.positionY = 0

    def draw(self):
        # Draw the car with rotation
        player = pygame.Rect((self.positionX - (self.carWidth / 2)), (self.positionY - (self.carHeight / 2)), self.carWidth, self.carHeight)
        rotated_image = pygame.transform.rotate(self.car_image, self.rotation_angle)
        rotated_rect = rotated_image.get_rect(center=player.center)
        self.screen.blit(rotated_image, rotated_rect.topleft)

    def get_speed(self):
        return self.speed