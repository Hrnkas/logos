import pygame
from turtle import Turtle # Import the Turtle class

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Logo Turtle"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0) # Added a color for the turtle

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Create a Turtle instance
# Position it at the center of the screen, initially pointing up (angle 0)
turtle = Turtle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, angle=0, color=RED)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Example: Basic keyboard controls for the turtle (optional for now, but good for testing)
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         turtle.forward(10)
        #     elif event.key == pygame.K_DOWN:
        #         turtle.backward(10)
        #     elif event.key == pygame.K_LEFT:
        #         turtle.left(15)
        #     elif event.key == pygame.K_RIGHT:
        #         turtle.right(15)


    # Update game state (placeholder)
    # Your game logic will go here

    # Draw graphics
    screen.fill(WHITE)  # Fill screen with white
    turtle.draw(screen) # Draw the turtle

    pygame.display.flip()  # Update the full display

    # Control frame rate
    clock.tick(60)  # 60 frames per second

# Quit Pygame
pygame.quit()
