import pygame

class DialogBox:
    def __init__(self, width, height, font):
        self.width = width
        self.height = height
        self.font = font
        self.active = False
        self.text = ""
        self.options = []
        self.selected_option = None

    def open(self, text, options=None, title=None):
        self.active = True
        self.text = text
        self.options = options or []
        self.selected_option = None
        self.title = title

    def close(self):
        self.active = False

    def handle_event(self, event):
        if not self.active:
            return
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            self.close()
        elif event.type == pygame.MOUSEBUTTONDOWN and self.options:
            mx, my = pygame.mouse.get_pos()
            for idx, rect in enumerate(self._option_rects()):
                if rect.collidepoint(mx, my):
                    self.selected_option = idx
                    self.close()

    def draw(self, screen):
        if not self.active:
            return
        # Grey out the screen (less dark)
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 100))
        screen.blit(overlay, (0, 0))

        # Draw dialog box
        box_rect = pygame.Rect(40, screen.get_height() - self.height - 40, self.width, self.height)
        pygame.draw.rect(screen, (40, 40, 40), box_rect)
        pygame.draw.rect(screen, (255, 255, 255), box_rect, 3)

        y_offset = box_rect.y + 20

        # Render title (NPC name)
        if hasattr(self, "title") and self.title:
            title_surf = self.font.render(self.title, True, (255, 255, 0))
            screen.blit(title_surf, (box_rect.x + 20, y_offset))
            y_offset += self.font.get_height() + 10

        # Render text
        lines = self._wrap_text(self.text, self.font, self.width - 40)
        for i, line in enumerate(lines):
            txt_surf = self.font.render(line, True, (255, 255, 255))
            screen.blit(txt_surf, (box_rect.x + 20, y_offset + i * (self.font.get_height() + 5)))

        # Render options
        if self.options:
            for idx, option in enumerate(self.options):
                opt_rect = self._option_rects()[idx]
                pygame.draw.rect(screen, (80, 80, 80), opt_rect)
                pygame.draw.rect(screen, (200, 200, 200), opt_rect, 2)
                opt_surf = self.font.render(option, True, (255, 255, 0))
                screen.blit(opt_surf, (opt_rect.x + 10, opt_rect.y + 5))

    def _option_rects(self):
        rects = []
        base_y = pygame.display.get_surface().get_height() - self.height + 40
        for idx, _ in enumerate(self.options):
            rects.append(pygame.Rect(60 + idx * 220, base_y, 200, 40))
        return rects

    def _wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = []
        current = ""
        for word in words:
            test = current + word + " "
            if font.size(test)[0] <= max_width:
                current = test
            else:
                lines.append(current)
                current = word + " "
        if current:
            lines.append(current)
        return lines
