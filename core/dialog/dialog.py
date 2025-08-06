import pygame
from config import *

class DialogBox:
    def __init__(self, font):
        self.font = font
        self.width = WINDOW_WIDTH
        self.height = BOX_HEIGHT
        self.active = False

        self.option_rects = []
        self.current_branch = None
        self.dialog_data = None
        self.selected_option_index = 0  # Track selected option
        self.title = ""

    def open(self, title, dialog_data):
        self.dialog_data = dialog_data
        self.title = title
        self.text = dialog_data.get("dialogue", "")
        self.options = dialog_data.get("options", [])
        self.selected_option_index = 0
        self.active = True

    def close(self):
        self.active = False

    def draw(self, screen):
        if not self.active:
            return

        box_rect = self._get_box_rect()
        self._draw_box_background(screen, box_rect)
        lines_rendered = self._draw_text(screen, box_rect)
        if self.options:
            self._draw_options(screen, box_rect, lines_rendered)

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
                title_text = f"{self.title}: "
                title_surface = self.font.render(title_text, True, TITLE_COLOR)
                screen.blit(title_surface, (x_pos, y_pos))

                text_surface = self.font.render(line, True, TEXT_COLOR)
                screen.blit(text_surface, (x_pos + title_surface.get_width(), y_pos))
            else:
                text_surface = self.font.render(line, True, TEXT_COLOR)
                screen.blit(text_surface, (x_pos, y_pos))

        return len(lines)

    def _draw_options(self, screen, box_rect, lines_rendered):
        self.option_rects = []
        line_height = self.font.get_height()

        y_start = box_rect.y + PADDING + (lines_rendered * (line_height + LINE_SPACING))
        x_start = box_rect.x + PADDING

        x_cursor = x_start
        y_cursor = y_start
        max_width = box_rect.width - (2 * PADDING)

        for i, option in enumerate(self.options):
            is_selected = (i == self.selected_option_index)
            color = SELECTED_COLOR if is_selected else TEXT_COLOR
            text_surface = self.font.render(option['text'], True, color)
            option_rect = text_surface.get_rect()

            if x_cursor + option_rect.width > box_rect.x + box_rect.width - PADDING:
                x_cursor = x_start
                y_cursor += line_height + VERTICAL_SPACING

            option_rect.x = x_cursor
            option_rect.y = y_cursor

            screen.blit(text_surface, option_rect)
            self.option_rects.append((option_rect, option))

            x_cursor += option_rect.width + HORIZONTAL_SPACING

    def handle_event(self, event):
        if not self.active or not self.options:
            return

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for rect, option in self.option_rects:
                if rect.collidepoint(mouse_pos):
                    self._handle_option_click(option)

    def _handle_option_click(self, option):
        next_key = option.get("next")
        if next_key and "branches" in self.dialog_data:
            next_data = self.dialog_data["branches"].get(next_key)
            if next_data:
                self.open(self.title, next_data)
        else:
            self.close()

    def _wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = []
        current_line = ""

        for word in words:
            test_line = f"{current_line}{word} " if current_line else f"{word} "

            if not lines and self.title:
                title_width = font.size(f"{self.title}: ")[0]
                available_width = max_width - title_width
            else:
                available_width = max_width

            if font.size(test_line)[0] <= available_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line.rstrip())
                current_line = f"{word} "

        if current_line:
            lines.append(current_line.rstrip())

        return lines

    # --- New: Keyboard selection methods ---

    def select_option_left(self):
        if self.options:
            self.selected_option_index = 0


    def select_option_right(self):
        if self.options:
            self.selected_option_index = 1

    def select_current_option(self):
        if self.options:
            selected_option = self.options[self.selected_option_index]
            self._handle_option_click(selected_option)
