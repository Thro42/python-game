import pygame
import sys
import math

class Player:
    def __init__(self, screen, posX, posY):
        # Initialize player attributes
        self.screen, self.positionX, self.positionY = screen, posX, posY
        self.speed, self.velocity = 0, 0.05
        self.carHeight, self.carWidth = 68, 36

        # Load and scale the car image
        self.car_image = pygame.transform.scale(pygame.image.load("CarRace/images/car-top_view.png"), (self.carWidth, self.carHeight))

        # Rotation properties
        self.rotation_angle, self.rotation_speed = 0, 1

        # Boundary and speed properties
        self.maxX, self.maxY, self.speedY = 800, 600, 0

        # Energy (health) properties
        self.max_energy, self.energy = 100, 100
        self.health_bar_width, self.health_bar_height = 200, 20
        self.health_bar_color = (255, 0, 0)

        # New property for deceleration
        self.deceleration = 0.1

    def rotate(self, direction):
        # Update rotation angle based on the direction
        self.rotation_angle += self.rotation_speed * direction

    def update_speed(self, factor):
        # Update speed based on the factor
        self.speed += self.velocity * factor

    def speed_up(self):
        # Accelerate the speed
        self.update_speed(1)

    def brake_up(self):
        # Decelerate the speed when braking
        self.update_speed(-3)

    def brake(self):
        # Gradually decelerate when the brake key is not pressed
        if self.speed > 0:
            self.update_speed(-self.deceleration)
        else:
            self.speed = 0

    def move(self):
        # Update player position based on current speed and rotation angle
        dx, dy = -math.sin(math.radians(self.rotation_angle)) * self.speed, -math.cos(math.radians(self.rotation_angle)) * self.speed
        self.speedY = dy
        new_positionX, new_positionY = self.positionX + dx, self.positionY + dy



        self.positionY = new_positionY
        if self.positionY < 300 :
            self.positionY = 300

        # Check if the new position is within the road boundaries
        if 140 <= new_positionX <= 665: #and 300 <= new_positionY <= self.maxY:
            self.positionX = new_positionX
        else:
            if new_positionX <= 140:
                self.positionX = new_positionX + 10
            if new_positionX > 665:
                self.positionX = new_positionX - 10
            self.speed -= 1
            # Reduce energy (health) when hitting the rails
            self.energy = max(0, self.energy - self.speed)
            # Reset position to prevent getting stuck in the rails
            #self.positionX, self.positionY = self.maxX / 2, self.maxY - 50

    def draw(self):
        #print("Y:", self.positionY )
        # Draw the rotated car image and the health bar
        player = pygame.Rect(self.positionX - self.carWidth / 2, self.positionY - self.carHeight / 2, self.carWidth, self.carHeight)
        rotated_image = pygame.transform.rotate(self.car_image, self.rotation_angle)
        rotated_rect = rotated_image.get_rect(center=player.center)
        self.screen.blit(rotated_image, rotated_rect.topleft)
        self.draw_health_bar()

    def draw_health_bar(self):
        # Draw the health bar based on the current energy level
        health_bar_width = int(self.energy / self.max_energy * self.health_bar_width)
        pygame.draw.rect(self.screen, self.health_bar_color, (10, 10, health_bar_width, self.health_bar_height), border_radius=5)

    def get_speed(self):
        return self.speed

    def get_speedY(self):
        return self.speedY

    def get_positionX(self):
        return self.positionX

    def get_energy(self):
        return self.energy

    def decrease_energy(self):
        # Decrease energy (health)
        self.energy -= 1
