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
YELLOW = (255, 255, 0) # For Clear Screen

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)


# Create a dedicated surface for drawing lines
drawing_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
drawing_surface.fill(WHITE) # Initial background for the drawing canvas

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Create a Turtle instance
# Adjust Y position to be in the drawable area, considering buttons at the bottom
# Buttons are ~50px high (40px + 10px margin). Let's center turtle in remaining space.
drawable_height = SCREEN_HEIGHT - 50
turtle = Turtle(SCREEN_WIDTH // 2, drawable_height // 2, angle=0, color=RED, drawing_surface=drawing_surface) # Pass drawing_surface

# --- Create Buttons ---
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 40
BUTTON_MARGIN = 10
BUTTON_Y = SCREEN_HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN # Y position for all buttons

# Define actions for the turtle
def action_forward():
    turtle.forward(20) # No longer pass 'screen' here

def action_left():
    turtle.left(30)

def action_right():
    turtle.right(30)

# --- Add new actions here ---
def action_pen_up():
    turtle.pen_up()

def action_pen_down():
    turtle.pen_down()

# --- Add new action here ---
def action_clear_screen():
    drawing_surface.fill(WHITE) # Clears the drawing canvas

    # Reset turtle's state
    # These values should match the turtle's initial instantiation values in main.py
    initial_x = SCREEN_WIDTH // 2
    initial_y = drawable_height // 2 # Match the calculation used at instantiation
    initial_angle = 0

    turtle.x = initial_x
    turtle.y = initial_y
    turtle.angle = initial_angle
    turtle.pen_down() # Reset to default pen state (drawing enabled)
# --- End new actions ---
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

# --- Define new Clear Screen button ---
clear_button_x = SCREEN_WIDTH - BUTTON_WIDTH - BUTTON_MARGIN
clear_button_y = BUTTON_MARGIN

button_clear_screen = Button(
    x=clear_button_x,
    y=clear_button_y,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    text="Clear Screen",
    color=YELLOW,
    text_color=BLACK,
    action=action_clear_screen
)

buttons.append(button_clear_screen)
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

        # --- Add Keyboard Event Handling Here ---
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                turtle.forward(20) # No longer pass 'screen' here
            elif event.key == pygame.K_LEFT:
                turtle.left(30) # Angle 30
            elif event.key == pygame.K_RIGHT:
                turtle.right(30) # Angle 30
        # --- End Keyboard Event Handling ---

    # Update game state
    # (Turtle state is updated by button actions via their callbacks or keyboard events)

    # Draw graphics
    screen.fill(WHITE)  # Clear main screen (especially if UI elements are drawn on it directly)

    # Blit the drawing_surface onto the main screen
    screen.blit(drawing_surface, (0, 0))

    # Draw the turtle icon itself (triangle) on the main screen
    turtle.draw(screen)

    # Draw buttons (on main screen)
    for btn in buttons:
        btn.draw(screen)

    pygame.display.flip()  # Update the full display

    # Control frame rate
    clock.tick(60)  # 60 frames per second

# Quit Pygame
pygame.quit()
