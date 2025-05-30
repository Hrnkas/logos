# Logo Turtle

A simple Logo-like programming environment using Python and Pygame.

This project creates a basic turtle graphics environment. Users can control a "turtle" cursor on the screen using UI buttons or keyboard shortcuts, making it draw lines as it moves (or not, depending on pen state). The turtle is visually represented by a triangle, which also provides feedback on the current pen state.

## Current Features
- A `Turtle` character that can be positioned and oriented on the screen.
- The turtle is rendered as a triangle.
  - **Visual Pen State Feedback:** The turtle triangle is drawn filled (black) when the pen is down, and as an outline (using its designated color) when the pen is up.
- **UI Buttons for Turtle and Pen Control:**
  - **Forward:** Moves the turtle forward. Draws a line if the pen is down.
  - **Turn Left:** Rotates the turtle to its left.
  - **Turn Right:** Rotates the turtle to its right.
  - **Pen Up:** Lifts the turtle's pen (turtle shown as outline), so it won't draw when moving.
  - **Pen Down:** Lowers the turtle's pen (turtle shown as filled shape), so it will draw when moving.
- **Keyboard Controls:**
  - Arrow keys for basic turtle movement (forward, turn left, turn right).
- Basic Pygame window setup.
- Line drawing when the turtle moves with the pen down (using the turtle's designated color).

## Controls
### UI Buttons
- **Forward Button:** Moves the turtle 20 units in its current direction.
- **Turn Left Button:** Rotates the turtle 30 degrees counter-clockwise.
- **Turn Right Button:** Rotates the turtle 30 degrees clockwise.
- **Pen Up Button:** Sets pen to "up" (turtle appears as outline, no drawing on move).
- **Pen Down Button:** Sets pen to "down" (turtle appears filled, drawing on move enabled).
### Keyboard Shortcuts
- **Up Arrow:** Moves the turtle forward by 20 units.
- **Left Arrow:** Rotates the turtle 30 degrees counter-clockwise.
- **Right Arrow:** Rotates the turtle 30 degrees clockwise.

## Features (Planned)
- More comprehensive turtle movement commands (e.g., specific distances, angles via input for both button and keyboard).
- Keyboard shortcuts for pen control.
- Color control for pen and turtle via UI (e.g., allowing the turtle's fill color to change).
- Clearing the screen.

## Running the Project

1. Ensure you have Python installed.
2. Create a virtual environment (optional but recommended):
   `python -m venv venv`
   `source venv/bin/activate`  # On Windows use `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the main file: `python logo_turtle/main.py`
