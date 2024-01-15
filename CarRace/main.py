import pygame
import sys
import math
import player

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

thePlayer = player.Player(screen, playerX, playerY)

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
speed_direction = 0
rotating_direction = 0


# Game Loop
while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           sys.exit()
       elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                acceleration = 0
                speed_direction = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rotating_direction = 0
       elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed_direction = 1
            elif event.key == pygame.K_DOWN:
                speed_direction = -1
            elif event.key == pygame.K_LEFT:
                rotating_direction = 1
            elif event.key == pygame.K_RIGHT:
                rotating_direction = -1

    thePlayer.rotate(rotating_direction)
    if speed_direction == 1:
        thePlayer.speed_up()
    elif speed_direction == -1:
        thePlayer.break_up()
    else:
        thePlayer.drive()


   # Update road position to create the illusion of movement
 #   road_y += speed


   # Reset road position when it goes beyond the image height
#   if road_y > road_image.get_height():
#       road_y = 0


   # Clear the screen
    screen.fill((192, 192, 192))  # Light Gray background


   # Draw the road
    screen.blit(road_image, (0, -road_y))
    screen.blit(road_image, (0, -road_y + road_image.get_height())) 


   # Draw the car with rotation
#   player = pygame.Rect((playerX - (carWidth / 2)), (playerY - (carHeight / 2)), carWidth, carHeight)
#   rotated_image = pygame.transform.rotate(car_image, rotation_angle)
#   rotated_rect = rotated_image.get_rect(center=player.center)
#   screen.blit(rotated_image, rotated_rect.topleft)
    thePlayer.move()
    thePlayer.draw()

    # Draw speed indicator
    speed = thePlayer.get_speed()
    speed_text = font.render(f"Speed: {speed:.2f}", True, (0, 0, 0))
    screen.blit(speed_text, (600, 20))


    pygame.display.update()
    clock.tick(60)
