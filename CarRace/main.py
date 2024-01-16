import pygame
import sys
import player
import road

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Create player and road instances
thePlayer = player.Player(screen, 400, 560)
theRoad = road.Road(screen)

# Load game over image
game_over_image = pygame.transform.scale(pygame.image.load("CarRace/images/game_over.png"), (800, 600))

# Initialize variables
road_y, speed_direction, rotating_direction, game_over = 0, 0, 0, False

# Game loop
while True:
    for event in pygame.event.get():
        # Handle events
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            # Handle key releases
            speed_direction = rotating_direction = 0
            thePlayer.brake()  # Call brake function when keys are released
        elif event.type == pygame.KEYDOWN:
            # Handle key presses
            speed_direction = 1 if event.key == pygame.K_UP else -1 if event.key == pygame.K_DOWN else speed_direction
            rotating_direction = 1 if event.key == pygame.K_LEFT else -1 if event.key == pygame.K_RIGHT else rotating_direction

    # Update player and road based on input
    thePlayer.rotate(rotating_direction)
    thePlayer.speed_up() if speed_direction == 1 else thePlayer.brake_up() if speed_direction == -1 else thePlayer.brake()
    theRoad.move(thePlayer.get_speedY())

    # Check for game over condition
    if thePlayer.get_energy() <= 0:
        game_over = True

    # Draw the game elements on the screen
   
    screen.fill((192, 192, 192))  # Light Gray background

    if not game_over:
        theRoad.draw()
        thePlayer.move()
        thePlayer.draw()
        speed_text = font.render(f"Speed: {thePlayer.get_speed():.2f}", True, (0, 0, 0))
        screen.blit(speed_text, (600, 20))
    else:
        # Display game over image
        screen.blit(game_over_image, (0, 0))

    pygame.display.update()
    clock.tick(60)
