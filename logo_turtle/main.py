import pygame
from .turtle import Turtle # Relative import
from .ui import Button # Relative import

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
PURPLE = (128, 0, 128) # For Undo button

# Button dimensions and positions
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 40
BUTTON_MARGIN = 10
BUTTON_Y = SCREEN_HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN # Y position for bottom row buttons

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
drawable_height = SCREEN_HEIGHT - 50
turtle = Turtle(SCREEN_WIDTH // 2, drawable_height // 2, angle=0, color=RED, drawing_surface=drawing_surface) # Pass drawing_surface

# Command history
command_history = [] # Initialize command history list

# --- Core Action-Handling Functions ---
def apply_turtle_action(command):
    action_type = command.get('action')
    value = command.get('value')

    if action_type == 'forward':
        turtle.forward(value) # turtle.forward now takes only distance
    elif action_type == 'left':
        turtle.left(value)
    elif action_type == 'right':
        turtle.right(value)
    elif action_type == 'pen_up':
        turtle.pen_up()
    elif action_type == 'pen_down':
        turtle.pen_down()
    # Add other actions here if any in the future (e.g., set_color)

def execute_and_store_command(command):
    apply_turtle_action(command)
    command_history.append(command)

def replay_history(history_to_replay):
    # 1. Clear the drawing surface
    drawing_surface.fill(WHITE)

    # 2. Reset the turtle to its initial state
    initial_x = SCREEN_WIDTH // 2
    initial_y = (SCREEN_HEIGHT - 100) // 2 # Consistent with turtle instantiation
    initial_angle = 0

    turtle.x = initial_x
    turtle.y = initial_y
    turtle.angle = initial_angle
    turtle.pen_down() # Default pen state

    # 3. Iterate through the provided history and apply each command
    for command_item in history_to_replay: # Renamed to avoid conflict with outer 'command'
        apply_turtle_action(command_item)

    # Note: The main game loop will handle blitting drawing_surface
    # and drawing the turtle icon in its final replayed state.

# --- Specific Action Callback Functions (for buttons/keys) ---
def action_forward():
    execute_and_store_command({'action': 'forward', 'value': 20})

def action_left():
    execute_and_store_command({'action': 'left', 'value': 30})

def action_right():
    execute_and_store_command({'action': 'right', 'value': 30})

def action_pen_up():
    execute_and_store_command({'action': 'pen_up'})

def action_pen_down():
    execute_and_store_command({'action': 'pen_down'})

def action_clear_screen():
    drawing_surface.fill(WHITE) # Clears the drawing canvas

    # Reset turtle's state
    initial_x = SCREEN_WIDTH // 2
    initial_y = (SCREEN_HEIGHT - 100) // 2
    initial_angle = 0

    turtle.x = initial_x
    turtle.y = initial_y
    turtle.angle = initial_angle
    turtle.pen_down()

    # Clear the command history
    command_history.clear()

def action_undo_last_command():
    if command_history: # Check if the list is not empty
        command_history.pop() # Remove the last command
        replay_history(command_history) # Replay the modified history
    else:
        pass # Do nothing if history is empty

# --- Create Buttons ---
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

button_pen_up = Button(
    x=BUTTON_MARGIN + (BUTTON_WIDTH + BUTTON_MARGIN) * 3,
    y=BUTTON_Y,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    text="Pen Up",
    color=ORANGE,
    action=action_pen_up
)

button_pen_down = Button(
    x=BUTTON_MARGIN + (BUTTON_WIDTH + BUTTON_MARGIN) * 4,
    y=BUTTON_Y,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    text="Pen Down",
    color=CYAN,
    text_color=BLACK,
    action=action_pen_down
)

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

undo_button_x = SCREEN_WIDTH - (BUTTON_WIDTH + BUTTON_MARGIN) * 2
undo_button_y = BUTTON_MARGIN
button_undo = Button(
    x=undo_button_x,
    y=undo_button_y,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    text="Undo",
    color=PURPLE,
    text_color=WHITE,
    action=action_undo_last_command
)

buttons = [button_forward, button_left, button_right, button_pen_up, button_pen_down, button_clear_screen, button_undo]

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pass event to buttons
        for btn in buttons:
            btn.handle_event(event)

        # Keyboard Event Handling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                execute_and_store_command({'action': 'forward', 'value': 20})
            elif event.key == pygame.K_LEFT:
                execute_and_store_command({'action': 'left', 'value': 30})
            elif event.key == pygame.K_RIGHT:
                execute_and_store_command({'action': 'right', 'value': 30})

    # Draw graphics
    screen.fill(WHITE)
    screen.blit(drawing_surface, (0, 0))
    turtle.draw(screen)

    for btn in buttons:
        btn.draw(screen)

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
