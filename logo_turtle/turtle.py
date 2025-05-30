import pygame
import math

class Turtle:
    def __init__(self, x, y, angle=0, color=(0, 0, 0)): # Default angle 0 (pointing up/north)
        self.x = x
        self.y = y
        self.angle = angle  # Angle in degrees, 0 is up (north), 90 is right (east)
        self.color = color
        self.is_pen_down = True # Pen is down by default

    def draw(self, surface):
        # Triangle points: base_left, base_right, tip
        # Turtle size
        size = 10 # Half the base width and height from center to tip/base_center

        # Convert angle to radians for math functions
        # Pygame's y-axis is inverted, so adjust angle calculation or point rotation
        # We'll define 0 degrees as pointing upwards (negative y-direction in Pygame)
        # and rotate clockwise.
        # math.sin and math.cos expect radians.
        # Angle: 0=Up, 90=Right, 180=Down, 270=Left
        
        # Center of the turtle
        center_x = self.x
        center_y = self.y

        # Points of the triangle relative to (0,0) assuming turtle points up (0 degrees)
        # Tip is 'size' units above the center
        # Base is 'size' units below the center, and 'size' units wide
        # For a triangle pointing up:
        # Tip: (0, -size*1.5) relative to turtle's x,y because y is inverted
        # Base Left: (-size, size*0.5)
        # Base Right: (size, size*0.5)

        # We want the turtle to be centered at self.x, self.y
        # Let's define points for an upward-pointing triangle centered at (0,0)
        # Tip: (0, -size * 2/3 * 2) -> (0, -4/3 * size)
        # Base Left: (-size, 2/3 * size)
        # Base Right: (size, 2/3 * size)
        # Let's use a simpler model: tip is (0, -size), base corners are (-size*0.75, size*0.5) and (size*0.75, size*0.5)
        
        # Points for a triangle pointing upwards (angle = 0) centered at (0,0)
        # Height of triangle = 2 * size, Base of triangle = 1.5 * size
        points_no_rotation = [
            (0, -size),                       # Tip
            (-size * 0.75, size * 0.5),       # Bottom-left
            (size * 0.75, size * 0.5),        # Bottom-right
        ]

        # Rotate points based on self.angle
        # Pygame's positive y is downwards. Standard math angle is counter-clockwise from positive x-axis.
        # Our angle: 0 is North (Up, -Y), 90 is East (Right, +X)
        # So, we need to convert our angle to standard math angle for rotation.
        # Math angle = 90 - Turtle angle (or (450 - Turtle angle) % 360)
        math_angle_rad = math.radians(90 - self.angle) 
        
        rotated_points = []
        for x_rel, y_rel in points_no_rotation:
            x_rot = x_rel * math.cos(math_angle_rad) - y_rel * math.sin(math_angle_rad)
            y_rot = x_rel * math.sin(math_angle_rad) + y_rel * math.cos(math_angle_rad)
            rotated_points.append((self.x + x_rot, self.y + y_rot))

        pygame.draw.polygon(surface, self.color, rotated_points)

    def forward(self, distance):
        # Convert angle to radians
        # Angle: 0=Up (-Y), 90=Right (+X)
        # dx = distance * sin(angle_rad)
        # dy = -distance * cos(angle_rad) (negative because Pygame y is inverted)
        rad_angle = math.radians(self.angle)
        delta_x = distance * math.sin(rad_angle)
        delta_y = -distance * math.cos(rad_angle) # Negative because screen Y is downwards
        
        new_x = self.x + delta_x
        new_y = self.y + delta_y
        
        # If pen is down, draw a line
        # For now, just update position. Line drawing will be part of a separate draw_line method or handled in main.
        # This 'forward' method is more about calculating the new position.
        
        self.x = new_x
        self.y = new_y

    def backward(self, distance):
        self.forward(-distance)

    def left(self, degrees):
        self.angle = (self.angle - degrees) % 360 # Subtract for left turn

    def right(self, degrees):
        self.angle = (self.angle + degrees) % 360 # Add for right turn

    def pen_up(self):
        self.is_pen_down = False

    def pen_down(self):
        self.is_pen_down = True

    def set_color(self, color):
        self.color = color
