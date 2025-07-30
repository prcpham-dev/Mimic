from config import WINDOW_WIDTH, WINDOW_HEIGHT
from core.player import Player
from core.background import Background
from core.dialog.dialog import DialogBox

import system.player_movement as player_movement
from core.task_manager import TaskManager

import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    font = pygame.font.SysFont("Arial", 28)
    pygame.display.set_caption("Mimic")
    clock = pygame.time.Clock()

    # Game objects
    player = Player()
    background = Background()
    
    # Dialog objects
    dialog = DialogBox(font)
    player.set_dialog(dialog)

    # Task manager object
    task_manager = TaskManager()

    running = True
    while running:
        events = pygame.event.get()

        # Handle quit
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        if task_manager.is_running():
            # Task logic
            task_manager.run(events)
            task_manager.draw(screen)
        else:
            # Normal room logic
            keys = pygame.key.get_pressed()
            player_movement.handle_input(player, keys, background)

            background.draw_background(screen)
            player.draw_player(screen)
            player.dialog.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
