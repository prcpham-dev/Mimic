import pygame
import config

class Player:
    def __init__(self):
        self.size = config.PLAYER_SIZE
        self.speed = config.PLAYER_SPEED

        # Load player image
        self.original_image = pygame.image.load(config.PLAYER_MODEL).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (self.size, self.size))
        self.image = self.original_image

        self.rect = self.image.get_rect()
        self.rect.center = (config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT // 2)

        self.isLeft = True
        self.held_item = None

    def handle_input(self, keys):
        # Left movement
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.isLeft = True
        # Right movement
        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.isLeft = False
        # Up movement
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        # Down movement
        if keys[pygame.K_s]:
            self.rect.y += self.speed

        # Flip image if facing right
        if self.isLeft:
            self.image = self.original_image
        else:
            self.image = pygame.transform.flip(self.original_image, True, False)

        # Clamp within screen bounds
        self.rect.x = max(5, 
                          min(self.rect.x, 
                          config.WINDOW_WIDTH - self.rect.width - 5))
        self.rect.y = max(5, 
                          min(self.rect.y, 
                              config.WINDOW_HEIGHT - self.rect.height - 5))

    def draw_player(self, screen):
        screen.blit(self.image, self.rect)
        # Draw held item if any
        if self.held_item:
            item_offset_x = self.size // 2 if not self.isLeft else -self.size // 2
            item_x = self.rect.centerx + item_offset_x
            item_y = self.rect.centery
            self.held_item.rect.center = (item_x, item_y)
            self.held_item.draw_item(screen, self.isLeft)
