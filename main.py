from config import WINDOW_WIDTH, WINDOW_HEIGHT
from core.player import Player
from core.background import Background

from system.interaction import handle_interaction
import system.player_movement as player_movement

import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pixel Art Game")
    clock = pygame.time.Clock()

    # Game objects
    player = Player()
    background = Background()

    running = True
    while running:
        # Movement
        keys = pygame.key.get_pressed()
        player_movement.handle_input(player, keys, background)

        # Drawing
        background.draw_background(screen)
        player.draw_player(screen)

        # Event loop: detect a single Enter press
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                handle_interaction(background, player)


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
