import pygame
from config import *

class DialogBox:
    def __init__(self, font):
        self.font = font
        self.width = WINDOW_WIDTH
        self.height = BOX_HEIGHT
        self.active = False

    def open(self, text, title, options=None):
        self.active = True
        self.title = title
        self.text = text
        self.options = options or []
        self.selected_option = None

    def close(self):
        self.active = False

    def draw(self, screen):
        if not self.active:
            return
        
        box_rect = self._get_box_rect()
        self._draw_box_background(screen, box_rect)
        self._draw_text(screen, box_rect)

    def _get_box_rect(self):
        x = MARGIN
        y = WINDOW_HEIGHT - self.height - MARGIN
        width = self.width - (2 * MARGIN)
        return pygame.Rect(x, y, width, self.height)

    def _draw_box_background(self, screen, box_rect):
        pygame.draw.rect(screen, BOX_COLOR, box_rect)
        pygame.draw.rect(screen, BORDER_COLOR, box_rect, BORDER_WIDTH)

    def _draw_text(self, screen, box_rect):
        lines = self._wrap_text(self.text, self.font, box_rect.width - (2 * PADDING))
        y_offset = box_rect.y + PADDING
        
        for i, line in enumerate(lines):
            x_pos = box_rect.x + PADDING
            y_pos = y_offset + (i * (self.font.get_height() + LINE_SPACING))
            
            if self.title and i == 0:
                title_surface = self.font.render(f"{self.title}: ", True, TITLE_COLOR)
                screen.blit(title_surface, (x_pos, y_pos))
                text_surface = self.font.render(line, True, TEXT_COLOR)
                title_width = title_surface.get_width()
                screen.blit(text_surface, (x_pos + title_width, y_pos))
            else:
                text_surface = self.font.render(line, True, TEXT_COLOR)
                screen.blit(text_surface, (x_pos, y_pos))

    def _wrap_text(self, text, font, max_width):
        """
        Handle long phrases.
        """
        words = text.split(' ')
        lines = []
        current_line = ""
        
        for word in words:
            test_line = f"{current_line}{word} " if current_line else f"{word} "
            
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line: 
                    lines.append(current_line.rstrip())
                current_line = f"{word} "
        
        if current_line:
            lines.append(current_line.rstrip())
            
        return lines