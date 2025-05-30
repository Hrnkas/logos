# Logo Turtle

A simple Logo-like programming environment using Python and Pygame.

This project creates a basic turtle graphics environment. Users can control a "turtle" cursor on the screen using UI buttons, making it draw lines as it moves. The turtle is visually represented by a triangle.

## Current Features
- A `Turtle` character that can be positioned and oriented on the screen.
- The turtle is rendered as a triangle.
- **UI Buttons for Turtle Control:**
  - **Forward:** Moves the turtle forward and draws a line if the pen is down.
  - **Turn Left:** Rotates the turtle to its left.
  - **Turn Right:** Rotates the turtle to its right.
- Basic Pygame window setup.
- Line drawing when the turtle moves with the pen down.

## Controls
- **Forward Button:** Moves the turtle 20 units in its current direction.
- **Turn Left Button:** Rotates the turtle 30 degrees counter-clockwise.
- **Turn Right Button:** Rotates the turtle 30 degrees clockwise.

## Features (Planned)
- More comprehensive turtle movement commands (e.g., specific distances, angles via input).
- Pen up/down control via UI.
- Color control for pen and turtle via UI.
- Clearing the screen.
- Keyboard shortcuts for controls.

## Running the Project

1. Ensure you have Python installed.
2. Create a virtual environment (optional but recommended):
   `python -m venv venv`
   `source venv/bin/activate`  # On Windows use `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the main file: `python logo_turtle/main.py`
