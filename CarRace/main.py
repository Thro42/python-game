import pygame
import sys
import math


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
speed = 0
playerX = 400
playerY = 560
carHeight = 68
carWidth = 36
rotation_angle = 0
angular_velocity = 0
acceleration = 0.05
deceleration = 0.02
max_speed = 5


# Load car image
car_image = pygame.image.load("CarRace/images/car-top_view.png")
car_image = pygame.transform.scale(car_image, (carWidth, carHeight))


# Load road image
road_image = pygame.image.load("CarRace/images/road.png")
road_image = pygame.transform.scale(road_image, (800, 1200))  # Make it taller than the screen


# Font setup
font = pygame.font.Font(None, 36)


# Initial road position
road_y = 0


# Game Loop
while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           sys.exit()
       elif event.type == pygame.KEYUP:
           if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
               acceleration = 0


   keys = pygame.key.get_pressed()


   if keys[pygame.K_UP]:
       acceleration = 0.05  # Move forward
   elif keys[pygame.K_DOWN]:
       acceleration = -0.05  # Move backward
   else:
       # Slow down if neither up nor down keys are pressed
       if speed > 0:
           acceleration = -deceleration
       else:
           acceleration = 0


   if speed >= 0:  # Check if the car is moving before allowing turning
       if keys[pygame.K_LEFT]:
           angular_velocity = 2  # Turn left
       elif keys[pygame.K_RIGHT]:
           angular_velocity = -2  # Turn right
       else:
           angular_velocity = 0
   else:
       angular_velocity = 0


   # Update angular velocity (turning)
   rotation_angle += angular_velocity


   # Update velocity components based on the angle
   dx = -math.sin(math.radians(rotation_angle)) * speed
   dy = -math.cos(math.radians(rotation_angle)) * speed  # Negative due to inverted Y-axis


   # Update speed based on acceleration and deceleration
   speed += acceleration
   if speed < 0:
       speed = 0
   elif speed > max_speed:
       speed = max_speed


   # Update player position
   playerX += dx
   playerY += dy


   # Update road position to create the illusion of movement
   road_y += speed


   # Reset road position when it goes beyond the image height
   if road_y > road_image.get_height():
       road_y = 0


   # Clear the screen
   screen.fill((192, 192, 192))  # Light Gray background


   # Draw the road
   screen.blit(road_image, (0, -road_y))
   screen.blit(road_image, (0, -road_y + road_image.get_height())) 


   # Draw the car with rotation
   player = pygame.Rect((playerX - (carWidth / 2)), (playerY - (carHeight / 2)), carWidth, carHeight)
   rotated_image = pygame.transform.rotate(car_image, rotation_angle)
   rotated_rect = rotated_image.get_rect(center=player.center)
   screen.blit(rotated_image, rotated_rect.topleft)


   # Draw speed indicator
   speed_text = font.render(f"Speed: {speed:.2f}", True, (0, 0, 0))
   screen.blit(speed_text, (600, 20))


   pygame.display.update()
   clock.tick(60)
