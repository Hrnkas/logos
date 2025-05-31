# Logo Turtle

A simple Logo-like programming environment using Python and Pygame.

This project creates a basic turtle graphics environment. Users can control a "turtle" cursor on the screen using UI buttons or keyboard shortcuts, making it draw lines as it moves (or not, depending on pen state). The turtle is visually represented by a triangle, which also provides feedback on the current pen state. The screen can be cleared of drawings using a dedicated button. The application features a main drawing canvas for the turtle and a side panel displaying a history of executed commands.

## Current Features
- A `Turtle` character that can be positioned and oriented on the screen.
- The turtle is rendered as a triangle.
  - **Visual Pen State Feedback:** The turtle triangle is drawn filled (black) when the pen is down, and as an outline (using its designated color) when the pen is up.
- **UI Buttons for Turtle, Pen, and Screen Control:**
  - **Forward:** Moves the turtle forward. Draws a line if the pen is down.
  - **Turn Left:** Rotates the turtle to its left.
  - **Turn Right:** Rotates the turtle to its right.
  - **Pen Up:** Lifts the turtle's pen (turtle shown as outline), so it won't draw when moving.
  - **Pen Down:** Lowers the turtle's pen (turtle shown as filled shape), so it will draw when moving.
  - **Clear Screen:** Clears all drawings and resets the turtle to its starting position, orientation (up), and pen state (down).
  - **Undo:** Reverts the last executed turtle action (movement, turn, or pen state change).
- **Keyboard Controls:**
  - Arrow keys for basic turtle movement (forward, turn left, turn right).
- **Command History Panel:**
  - The screen is divided into a main drawing area (left) and a panel on the right.
  - This panel displays a list of the recently executed commands (e.g., "FORWARD 20", "PEN UP").
  - The history updates dynamically as commands are performed or undone. Clearing the screen also clears the history.
- Basic Pygame window setup.
- Line drawing when the turtle moves with the pen down (using the turtle's designated color).

## Controls
### UI Buttons
- **Forward Button:** Moves the turtle 20 units in its current direction.
- **Turn Left Button:** Rotates the turtle 30 degrees counter-clockwise.
- **Turn Right Button:** Rotates the turtle 30 degrees clockwise.
- **Pen Up Button:** Sets pen to "up" (turtle appears as outline, no drawing on move).
- **Pen Down Button:** Sets pen to "down" (turtle appears filled, drawing on move enabled).
- **Clear Screen Button:** (Top-right corner) Clears all turtle drawings from the screen and resets the turtle to its initial position (center), orientation (up), and pen state (down).
- **Undo Button:** (Top-right area, near Clear Screen) Reverses the last turtle command (Forward, Left, Right, Pen Up, Pen Down). The command history is cleared when "Clear Screen" is used.
### Keyboard Shortcuts
- **Up Arrow:** Moves the turtle forward by 20 units.
- **Left Arrow:** Rotates the turtle 30 degrees counter-clockwise.
- **Right Arrow:** Rotates the turtle 30 degrees clockwise.

## Features (Planned)
- More comprehensive turtle movement commands (e.g., specific distances, angles via input for both button and keyboard).
- Keyboard shortcuts for pen control.
- Color control for pen and turtle via UI (e.g., allowing the turtle's fill color to change).
- Potential refactor to a persistent drawing surface for more advanced features.

## Running the Project

1.  Ensure you have Python installed.
2.  Navigate to the **root directory** of this project in your terminal.
3.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4.  Install dependencies from the virtual environment:
    ```bash
    pip install -r requirements.txt
    ```
5.  Run the application from the **project's root directory**:
    ```bash
    python -m logo_turtle.main
    ```

## Building the Executable (Windows)

This project can be compiled into a Windows executable using PyInstaller. A batch script is provided to automate this process.

**Prerequisites:**
- Python installed and added to your PATH.

**Build Steps:**

1.  **Open Command Prompt:** Navigate to the root directory of the project in your command prompt.
2.  **Run the build script:**
    ```bash
    build.bat
    ```
    This script will:
    - Create a local virtual environment named `venv_build`.
    - Install dependencies from `requirements.txt` and `requirements-dev.txt` (which includes `pyinstaller`).
    - Run `pyinstaller` to package the application.
3.  **Find the Executable:**
    - Upon successful completion, the executable will be located in the `dist\LogoTurtle` folder. You can run `LogoTurtle.exe` from there.
    - The `build` folder and `*.spec` file are temporary files created by PyInstaller and can be ignored (they will be removed by the `--clean` option on the next build or can be added to `.gitignore`).

**Notes:**
- The build script currently creates a one-folder bundle (`--onedir`). This means it generates a folder with the main executable and its dependencies.
- If you wish to add a custom icon, you can place an `.ico` file (e.g., in an `assets` directory) and uncomment/modify the `ICON_PATH` variable and the `--icon` option in `build.bat`.
