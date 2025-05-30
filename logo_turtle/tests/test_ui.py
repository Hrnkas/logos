import unittest
import pygame
from unittest.mock import MagicMock # For mocking callback actions

# Adjust import path if your project structure is different.
# Assuming 'logo_turtle' is a package in PYTHONPATH.
from logo_turtle.ui import Button 

class TestButton(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize Pygame modules needed for Button (specifically font)
        pygame.init() 

    @classmethod
    def tearDownClass(cls):
        # Quit Pygame after all tests in the class are done
        pygame.quit()

    def test_button_creation_defaults(self):
        button = Button(x=10, y=20, width=100, height=50)
        self.assertEqual(button.rect.x, 10)
        self.assertEqual(button.rect.y, 20)
        self.assertEqual(button.rect.width, 100)
        self.assertEqual(button.rect.height, 50)
        self.assertEqual(button.text, 'Button') # Default text
        self.assertEqual(button.color, (200, 200, 200)) # Default color
        self.assertIsNone(button.action)
        self.assertFalse(button.is_hovered)

    def test_button_creation_custom(self):
        mock_action = MagicMock()
        button = Button(
            x=5, y=15, width=120, height=60, 
            text='Click Me', 
            color=(0, 255, 0), 
            text_color=(255, 0, 0), 
            action=mock_action,
            font_size=24
        )
        self.assertEqual(button.rect.x, 5)
        self.assertEqual(button.text, 'Click Me')
        self.assertEqual(button.color, (0, 255, 0))
        self.assertEqual(button.text_color, (255, 0, 0))
        self.assertEqual(button.action, mock_action)
        self.assertEqual(button.font.get_height(), pygame.font.Font(None, 24).get_height())


    def test_is_clicked_positive(self):
        button = Button(x=10, y=10, width=100, height=50)
        # Click inside the button
        self.assertTrue(button.is_clicked((50, 30))) 
        # Click on edge
        self.assertTrue(button.is_clicked((10, 10)))
        self.assertTrue(button.is_clicked((110-1, 60-1))) # rect.collidepoint is exclusive for right/bottom edge

    def test_is_clicked_negative(self):
        button = Button(x=10, y=10, width=100, height=50)
        # Click outside
        self.assertFalse(button.is_clicked((5, 5)))
        self.assertFalse(button.is_clicked((110, 60))) # Exactly on edge or outside

    def test_handle_event_mouse_motion_hover(self):
        button = Button(x=10, y=10, width=100, height=50)
        
        # Mouse moves onto button
        event_motion_over = pygame.event.Event(pygame.MOUSEMOTION, {'pos': (50, 30)})
        button.handle_event(event_motion_over)
        self.assertTrue(button.is_hovered)

        # Mouse moves off button
        event_motion_away = pygame.event.Event(pygame.MOUSEMOTION, {'pos': (5, 5)})
        button.handle_event(event_motion_away)
        self.assertFalse(button.is_hovered)

    def test_handle_event_click_no_action(self):
        button = Button(x=10, y=10, width=100, height=50) # No action defined
        
        # Simulate hover first
        event_motion_over = pygame.event.Event(pygame.MOUSEMOTION, {'pos': (50, 30)})
        button.handle_event(event_motion_over)

        event_click = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'button': 1, 'pos': (50, 30)})
        result = button.handle_event(event_click)
        self.assertTrue(result) # Event handled (click was on button)
        # No action to call, so nothing to assert there beyond no error

    def test_handle_event_click_with_action(self):
        mock_action = MagicMock()
        button = Button(x=10, y=10, width=100, height=50, action=mock_action)
        
        # Simulate hover
        event_motion_over = pygame.event.Event(pygame.MOUSEMOTION, {'pos': (50, 30)})
        button.handle_event(event_motion_over)
        
        # Simulate click
        event_click = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'button': 1, 'pos': (50, 30)})
        result = button.handle_event(event_click)
        
        self.assertTrue(result) # Event handled
        mock_action.assert_called_once() # Check that the action was called

    def test_handle_event_click_outside(self):
        mock_action = MagicMock()
        button = Button(x=10, y=10, width=100, height=50, action=mock_action)
        
        event_click_outside = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'button': 1, 'pos': (5, 5)})
        result = button.handle_event(event_click_outside)
        
        self.assertFalse(result) # Event not handled by this button
        mock_action.assert_not_called()

    def test_handle_event_non_click_or_motion(self):
        mock_action = MagicMock()
        button = Button(x=10, y=10, width=100, height=50, action=mock_action)
        
        event_other = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_SPACE})
        result = button.handle_event(event_other)
        
        self.assertFalse(result) # Event not handled
        mock_action.assert_not_called()
        self.assertFalse(button.is_hovered) # Hover state should not change

    def test_draw_runs_without_error(self):
        button = Button(x=10, y=10, width=100, height=50)
        mock_surface = pygame.Surface((200, 200))
        try:
            button.draw(mock_surface)
        except Exception as e:
            self.fail(f"button.draw() raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
