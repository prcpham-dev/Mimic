import pygame
import sys
from config import WINDOW_WIDTH, WINDOW_HEIGHT

from core.player import Player
from core.background import Background

from core.interactable.npc import npc
from core.interactable.item import ItemInteract

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

    # List of items

    items = [
        ItemInteract(100, 100, 100, 200, (255, 200, 150)),
        npc(300, 200, 50, 50, (150, 200, 255), "Bob", "Hello there!"),
        ItemInteract(500, 350, 40, 40, (255, 100, 100))
    ]

    # Font for interaction prompt
    font = pygame.font.SysFont(None, 24)

    running = True
    while running:
        enter_pressed = False

        # Event loop: detect a single Enter press
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                enter_pressed = True

        # Drawing
        background.draw_background(screen)

        for item in items:
            item.draw_item(screen)

        player.draw_player(screen)
        
        # Movement
        keys = pygame.key.get_pressed()
        player.handle_input(keys)

        # Interactions (only if Enter was just pressed)
        if enter_pressed:
            for item in items:
                if is_player_near(item, player):
                    item.interact(player)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()