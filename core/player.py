import pygame
import config

class Player:
    def __init__(self):
        self.size = config.PLAYER_SIZE
        self.color = config.PLAYER_COLOR
        self.speed = config.PLAYER_SPEED

        self.rect = pygame.Rect(
            config.WINDOW_WIDTH // 2,
            config.WINDOW_HEIGHT // 2,
            self.size,
            self.size
        )

    def handle_input(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

        # Clamp within screen bounds
        self.rect.x = max(5, 
                          min(self.rect.x, 
                          config.WINDOW_WIDTH - self.rect.width - 5))
        self.rect.y = max(5, 
                          min(self.rect.y, 
                              config.WINDOW_HEIGHT - self.rect.height - 5))

    def draw_player(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
