import pygame
from logo_turtle.turtle import Turtle
from logo_turtle.ui import Button # Import Button

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 # Increased height to make space for buttons
SCREEN_TITLE = "Logo Turtle"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0) # For Forward button
BLUE = (0, 0, 200)  # For Turn buttons
LIGHT_GREY = (220, 220, 220)
ORANGE = (255, 165, 0) # For Pen Up
CYAN = (0, 255, 255)   # For Pen Down

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Create a Turtle instance
# Adjust Y position to be in the drawable area, considering buttons at the bottom
# Buttons are ~50px high (40px + 10px margin). Let's center turtle in remaining space.
drawable_height = SCREEN_HEIGHT - 50 
turtle = Turtle(SCREEN_WIDTH // 2, drawable_height // 2, angle=0, color=RED)

# --- Create Buttons ---
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 40
BUTTON_MARGIN = 10
BUTTON_Y = SCREEN_HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN # Y position for all buttons

# Define actions for the turtle
def action_forward():
    turtle.forward(20, screen) # Pass screen object

def action_left():
    turtle.left(30)

def action_right():
    turtle.right(30)

# --- Add new actions here ---
def action_pen_up():
    turtle.pen_up()

def action_pen_down():
    turtle.pen_down()
# --- End new actions ---

button_forward = Button(
    x=BUTTON_MARGIN,
    y=BUTTON_Y,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    text="Forward",
    color=GREEN,
    action=action_forward
)

button_left = Button(
    x=BUTTON_MARGIN + BUTTON_WIDTH + BUTTON_MARGIN,
    y=BUTTON_Y,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    text="Left",
    color=BLUE,
    text_color=WHITE,
    action=action_left
)

button_right = Button(
    x=BUTTON_MARGIN + (BUTTON_WIDTH + BUTTON_MARGIN) * 2,
    y=BUTTON_Y,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    text="Right",
    color=BLUE,
    text_color=WHITE,
    action=action_right
)

# --- Define new Pen Up / Pen Down buttons ---
button_pen_up = Button(
    x=BUTTON_MARGIN + (BUTTON_WIDTH + BUTTON_MARGIN) * 3, # Position after Right button
    y=BUTTON_Y,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    text="Pen Up",
    color=ORANGE,
    action=action_pen_up
)

button_pen_down = Button(
    x=BUTTON_MARGIN + (BUTTON_WIDTH + BUTTON_MARGIN) * 4, # Position after Pen Up button
    y=BUTTON_Y,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    text="Pen Down",
    color=CYAN,
    text_color=BLACK, # Ensure text is visible
    action=action_pen_down
)

# Add new buttons to the list
buttons = [button_forward, button_left, button_right, button_pen_up, button_pen_down]
# --- End button updates ---

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Pass event to buttons
        for btn in buttons:
            btn.handle_event(event) # handle_event will call the action if button is clicked

    # Update game state 
    # (Turtle state is updated by button actions via their callbacks)

    # Draw graphics
    screen.fill(WHITE)  # Fill screen with white
    
    turtle.draw(screen) # Draw the turtle
    
    # Draw buttons
    for btn in buttons:
        btn.draw(screen)

    pygame.display.flip()  # Update the full display

    # Control frame rate
    clock.tick(60)  # 60 frames per second

# Quit Pygame
pygame.quit()
