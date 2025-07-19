from config import WINDOW_WIDTH, WINDOW_HEIGHT, INTERACT_RANGE
from core.player import Player
from core.background import Background

import pygame
import sys

def is_player_near(item, player):
    expanded_rect = player.rect.inflate(INTERACT_RANGE * 2, INTERACT_RANGE * 2)
    return expanded_rect.colliderect(item.rect)

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
            for item in background.items:
                if is_player_near(item, player) and item.activated:
                    item.interact(player)
                    break

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()