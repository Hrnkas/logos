# Logo Turtle

A simple Logo-like programming environment using Python and Pygame.

This project creates a basic turtle graphics environment. Users can control a "turtle" cursor on the screen using UI buttons or keyboard shortcuts, making it draw lines as it moves (or not, depending on pen state). The turtle is visually represented by a triangle.

## Current Features
- A `Turtle` character that can be positioned and oriented on the screen.
- The turtle is rendered as a triangle.
- **UI Buttons for Turtle and Pen Control:**
  - **Forward:** Moves the turtle forward. Draws a line if the pen is down.
  - **Turn Left:** Rotates the turtle to its left.
  - **Turn Right:** Rotates the turtle to its right.
  - **Pen Up:** Lifts the turtle's pen, so it won't draw when moving.
  - **Pen Down:** Lowers the turtle's pen, so it will draw when moving (default state).
- **Keyboard Controls:**
  - Arrow keys for basic turtle movement (forward, turn left, turn right).
- Basic Pygame window setup.
- Line drawing when the turtle moves with the pen down.

## Controls
### UI Buttons
- **Forward Button:** Moves the turtle 20 units in its current direction.
- **Turn Left Button:** Rotates the turtle 30 degrees counter-clockwise.
- **Turn Right Button:** Rotates the turtle 30 degrees clockwise.
- **Pen Up Button:** Toggles the pen state to "up" (no drawing).
- **Pen Down Button:** Toggles the pen state to "down" (drawing enabled).
### Keyboard Shortcuts
- **Up Arrow:** Moves the turtle forward by 20 units.
- **Left Arrow:** Rotates the turtle 30 degrees counter-clockwise.
- **Right Arrow:** Rotates the turtle 30 degrees clockwise.

## Features (Planned)
- More comprehensive turtle movement commands (e.g., specific distances, angles via input for both button and keyboard).
- Keyboard shortcuts for pen control.
- Color control for pen and turtle via UI.
- Clearing the screen.
- Visual feedback for current pen state.

## Running the Project

1. Ensure you have Python installed.
2. Create a virtual environment (optional but recommended):
   `python -m venv venv`
   `source venv/bin/activate`  # On Windows use `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the main file: `python logo_turtle/main.py`
