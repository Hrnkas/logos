import unittest
import pygame # Pygame needed for surface for drawing, and color
from logo_turtle.turtle import Turtle # Adjust import path as necessary

class TestTurtle(unittest.TestCase):

    def setUp(self):
        # Pygame needs to be initialized to create a Surface
        pygame.init() 
        # Create a dummy surface for the turtle to be "drawn" on, if needed for tests.
        # Some methods might not need a surface, but draw() does.
        self.mock_surface = pygame.Surface((100, 100))

    def test_initial_state(self):
        turtle = Turtle(x=50, y=60, angle=90, color=(255,0,0))
        self.assertEqual(turtle.x, 50)
        self.assertEqual(turtle.y, 60)
        self.assertEqual(turtle.angle, 90)
        self.assertEqual(turtle.color, (255,0,0))
        self.assertTrue(turtle.is_pen_down) # Default pen state

    def test_initial_state_defaults(self):
        # Test with default angle and color
        turtle = Turtle(x=10, y=20)
        self.assertEqual(turtle.x, 10)
        self.assertEqual(turtle.y, 20)
        self.assertEqual(turtle.angle, 0) # Default angle
        self.assertEqual(turtle.color, (0,0,0)) # Default color
        self.assertTrue(turtle.is_pen_down)

    def test_forward_movement(self):
        turtle = Turtle(x=0, y=0, angle=0) # Pointing up
        turtle.forward(10)
        self.assertAlmostEqual(turtle.x, 0) # No change in X when pointing up
        self.assertAlmostEqual(turtle.y, -10) # Moves -10 in Y (up)

        turtle = Turtle(x=0, y=0, angle=90) # Pointing right
        turtle.forward(10)
        self.assertAlmostEqual(turtle.x, 10) # Moves +10 in X
        self.assertAlmostEqual(turtle.y, 0)  # No change in Y

        turtle = Turtle(x=0, y=0, angle=45) # Pointing up-right
        turtle.forward(10)
        expected_dx = 10 * pygame.math.Vector2(0, -1).rotate(-45).x # Standard math: (1,0) rotated by angle. Pygame: (0,-1) rotated by -angle
        expected_dy = 10 * pygame.math.Vector2(0, -1).rotate(-45).y
        # self.assertAlmostEqual(turtle.x, 10 * math.sin(math.radians(45)))
        # self.assertAlmostEqual(turtle.y, -10 * math.cos(math.radians(45)))
        self.assertAlmostEqual(turtle.x, expected_dx)
        self.assertAlmostEqual(turtle.y, expected_dy)


    def test_backward_movement(self):
        turtle = Turtle(x=0, y=0, angle=0) # Pointing up
        turtle.backward(10)
        self.assertAlmostEqual(turtle.x, 0)
        self.assertAlmostEqual(turtle.y, 10) # Moves +10 in Y (down)

        turtle = Turtle(x=0, y=0, angle=90) # Pointing right
        turtle.backward(10)
        self.assertAlmostEqual(turtle.x, -10) # Moves -10 in X
        self.assertAlmostEqual(turtle.y, 0)

    def test_left_turn(self):
        turtle = Turtle(x=0, y=0, angle=90)
        turtle.left(30)
        self.assertEqual(turtle.angle, 60)
        turtle.left(70) # Test wrapping around 0
        self.assertEqual(turtle.angle, 350) # 60 - 70 = -10 which is 350

    def test_right_turn(self):
        turtle = Turtle(x=0, y=0, angle=30)
        turtle.right(60)
        self.assertEqual(turtle.angle, 90)
        turtle.right(300) # Test wrapping around 360
        self.assertEqual(turtle.angle, 30) # 90 + 300 = 390 which is 30

    def test_pen_controls(self):
        turtle = Turtle(x=0, y=0)
        self.assertTrue(turtle.is_pen_down) # Default
        turtle.pen_up()
        self.assertFalse(turtle.is_pen_down)
        turtle.pen_down()
        self.assertTrue(turtle.is_pen_down)

    def test_set_color(self):
        turtle = Turtle(x=0, y=0)
        new_color = (10, 20, 30)
        turtle.set_color(new_color)
        self.assertEqual(turtle.color, new_color)

    def test_draw_runs_without_error(self):
        turtle = Turtle(x=50, y=50)
        try:
            turtle.draw(self.mock_surface)
        except Exception as e:
            self.fail(f"turtle.draw() raised an exception: {e}")
            
    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
