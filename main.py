from config import WINDOW_WIDTH, WINDOW_HEIGHT
from core.player import Player
from core.background import Background
from core.dialog.dialog import DialogBox
from core.game import Game

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
    game = Game()

    # Game objects
    game.set_player(Player())
    game.set_background(Background())
    
    # Dialog objects
    game.set_dialog(DialogBox(font))

    # Task manager object
    game.set_task_manager(TaskManager())

    running = True
    while running:
        events = pygame.event.get()

        # Handle quit
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        if game.task_manager.is_running():
            # Task logic
            game.task_manager.run(events)
            game.task_manager.draw(screen)
        else:
            # Normal room logic
            keys = pygame.key.get_pressed()
            player_movement.handle_input(keys, game)

            game.background.draw_background(screen)
            game.player.draw_player(screen)
            game.dialog.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
