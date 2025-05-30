import pygame

class Button:
    def __init__(self, x, y, width, height, text='Button', color=(200, 200, 200), text_color=(0, 0, 0), action=None, font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.action = action
        self.font = pygame.font.Font(None, font_size) # Use default system font
        self.is_hovered = False

    def draw(self, surface):
        # Change color if hovered
        draw_color = self.color
        if self.is_hovered:
            # Slightly darken the button color when hovered
            draw_color = (max(0, self.color[0] - 30),
                          max(0, self.color[1] - 30),
                          max(0, self.color[2] - 30))

        pygame.draw.rect(surface, draw_color, self.rect)
        pygame.draw.rect(surface, self.text_color, self.rect, 2) # Border

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        # Check for hover
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.is_hovered = True
            else:
                self.is_hovered = False

        # Check for click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.is_clicked(event.pos): # event.button == 1 means left click
                if self.action:
                    self.action() # Execute the button's action
                return True # Indicate that the event was handled by this button
        return False # Event not handled by this button
