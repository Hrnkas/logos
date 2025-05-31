import pygame
from .turtle import Turtle # Relative import
from .ui import Button # Relative import

# Initialize Pygame
pygame.init()

# Screen dimensions
# SCREEN_WIDTH = 800 # Old width
SCREEN_HEIGHT = 600  # Original height
DRAWING_AREA_WIDTH = 800 # Original screen width becomes drawing area
COMMAND_PANEL_WIDTH = 250
SCREEN_WIDTH = DRAWING_AREA_WIDTH + COMMAND_PANEL_WIDTH # New total width
COMMAND_PANEL_X_START = DRAWING_AREA_WIDTH
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

# Command Panel constants
PANEL_BG_COLOR = (230, 230, 230)
PANEL_TEXT_COLOR = (0, 0, 0)
PANEL_BORDER_COLOR = (180, 180, 180)
MAX_HISTORY_DISPLAY = 20 # Max number of commands to show

# Button dimensions and positions
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 40
BUTTON_MARGIN = 10
BUTTON_Y = SCREEN_HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN # Y position for bottom row buttons

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Uses new total SCREEN_WIDTH
pygame.display.set_caption(SCREEN_TITLE)

# Create a dedicated surface for drawing lines
drawing_surface = pygame.Surface((DRAWING_AREA_WIDTH, SCREEN_HEIGHT)) # Uses DRAWING_AREA_WIDTH
drawing_surface.fill(WHITE) # Initial background for the drawing canvas

# Clock for controlling frame rate
clock = pygame.time.Clock()
history_font = pygame.font.Font(None, 24) # Font for command history panel

# Create a Turtle instance
# Adjust Y position to be in the drawable area, considering buttons at the bottom
drawable_height = SCREEN_HEIGHT - 50
turtle = Turtle(DRAWING_AREA_WIDTH // 2, drawable_height // 2, angle=0, color=RED, drawing_surface=drawing_surface) # Use DRAWING_AREA_WIDTH

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
    initial_x = DRAWING_AREA_WIDTH // 2 # Use DRAWING_AREA_WIDTH
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
    initial_x = DRAWING_AREA_WIDTH // 2 # Use DRAWING_AREA_WIDTH
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

def format_command_for_display(command):
    action = command.get('action', 'UNKNOWN').upper()
    value = command.get('value', '')
    if action in ['FORWARD', 'LEFT', 'RIGHT']:
        return f"{action} {value}"
    elif action in ['PEN_UP', 'PEN_DOWN']:
        return action.replace('_', ' ')
    return action # Default for unknown or valueless actions

def draw_command_panel(surface, rect, command_hist, text_font):
    # Draw panel background
    pygame.draw.rect(surface, PANEL_BG_COLOR, rect)
    pygame.draw.rect(surface, PANEL_BORDER_COLOR, rect, 2) # Border

    # Title
    title_text = "Command History"
    title_surf = text_font.render(title_text, True, PANEL_TEXT_COLOR)
    title_rect = title_surf.get_rect(centerx=rect.centerx, top=rect.top + 5)
    surface.blit(title_surf, title_rect)

    # Display commands (latest at the bottom)
    start_y = title_rect.bottom + 10
    line_height = text_font.get_linesize()

    # Display up to MAX_HISTORY_DISPLAY commands
    # Take the last MAX_HISTORY_DISPLAY items from history
    display_history = command_hist[-MAX_HISTORY_DISPLAY:]

    for i, command_item in enumerate(display_history): # Use command_item to avoid conflict
        command_str = f"{i+1}. {format_command_for_display(command_item)}" # Add numbering
        command_surf = text_font.render(command_str, True, PANEL_TEXT_COLOR)
        # Position text line by line
        text_pos_y = start_y + (i * line_height)
        # Check if text exceeds panel height (minus some padding)
        if text_pos_y + line_height > rect.bottom - 5:
            break # Stop if no more space

        surface.blit(command_surf, (rect.left + 10, text_pos_y))

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

# Position Clear Screen button (centered at top of command panel)
clear_button_x = COMMAND_PANEL_X_START + (COMMAND_PANEL_WIDTH - BUTTON_WIDTH) // 2
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

# Position Undo button (below Clear Screen, centered in command panel)
undo_button_x = COMMAND_PANEL_X_START + (COMMAND_PANEL_WIDTH - BUTTON_WIDTH) // 2
undo_button_y = BUTTON_MARGIN + BUTTON_HEIGHT + BUTTON_MARGIN
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
    screen.fill(WHITE)  # Clear main screen (or fill with a UI background color)

    # Blit the drawing_surface (where turtle lines are) onto the main screen
    screen.blit(drawing_surface, (0, 0))

    # Draw the turtle icon itself (triangle) on the main screen
    turtle.draw(screen)

    # --- Draw Command History Panel ---
    panel_rect = pygame.Rect(COMMAND_PANEL_X_START, 0, COMMAND_PANEL_WIDTH, SCREEN_HEIGHT)
    draw_command_panel(screen, panel_rect, command_history, history_font) # Draw panel
    # --- End Panel Drawing ---

    # Draw buttons (on main screen)
    # Buttons like Clear and Undo are expected to be on top of the panel background
    for btn in buttons:
        btn.draw(screen)

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
