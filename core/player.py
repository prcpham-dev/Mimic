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
        # Move left
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.isLeft = True
        # Move right
        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.isLeft = False
        # Move up
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        # Move down
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        

    def draw_player(self, screen):
        # Flip player image based on direction
        if self.isLeft:
            self.image = self.original_image
        else:
            self.image = pygame.transform.flip(self.original_image, True, False)

        # Draw player
        screen.blit(self.image, self.rect)
        if self.held_item:
            self.held_item.flip_item(self.isLeft)

            # Position item relative to player
            item_offset_x = self.size // 2 if not self.isLeft else -self.size // 2
            item_x = self.rect.centerx + item_offset_x
            item_y = self.rect.centery
            self.held_item.rect.center = (item_x, item_y)

            # Draw the held item
            screen.blit(self.held_item.image, self.held_item.rect)


