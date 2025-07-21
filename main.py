from config import WINDOW_WIDTH, WINDOW_HEIGHT
from core.player import Player
from core.background import Background
from core.dialog.dialog import DialogBox

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
    
    font = pygame.font.SysFont("Arial", 28)
    dialog = DialogBox(WINDOW_WIDTH, 120, font)
    player.set_dialog(dialog)
    
    running = True
    while running:
        # Keybinds
        keys = pygame.key.get_pressed()
        player_movement.handle_input(player, keys, background)

        # Drawing
        background.draw_background(screen)
        player.draw_player(screen)
        player.dialog.draw(screen)

        # Event loop: detect closing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
