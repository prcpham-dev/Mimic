from config import WINDOW_WIDTH, WINDOW_HEIGHT
from core.player import Player
from core.background import Background

import pygame
import sys

def is_player_near(item, player):
    return item.rect.colliderect(player.rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pixel Art Game")
    clock = pygame.time.Clock()

    # Game objects
    player = Player()
    background = Background()

    # Font for interaction prompt
    font = pygame.font.SysFont(None, 24)

    running = True
    while running:
        enter_pressed = False

        # Movement
        keys = pygame.key.get_pressed()
        player.handle_input(keys)

        # Drawing
        background.draw_background(screen)
        player.draw_player(screen)

        # Event loop: detect a single Enter press
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                enter_pressed = True

        # Interactions (only if Enter was just pressed)
        if enter_pressed:
            # Find nearest item to player
            nearby_items = [item for item in background.items if is_player_near(item, player)]
            if nearby_items:
                # Sort by distance to player center
                nearest = min(nearby_items, key=lambda item: ((item.rect.centerx - player.rect.centerx) ** 2 + (item.rect.centery - player.rect.centery) ** 2))
                nearest.interact(player)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
