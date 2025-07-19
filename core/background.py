import pygame
import config
from core.interactable.item import Item
from core.interactable.npc import npc

class Background:
    def __init__(self):
        self.color = config.BACKGROUND_COLOR
        self.items = self._load_items()

    def draw_background(self, screen):
        screen.fill((0, 0, 0))
        self.draw_items(screen)

    def _load_items(self):
        return [
            Item("Sword", 100, 100, "assets/sword.png"),
            npc("Bob", 300, 200, "assets/npc.png", "Hello there!"),
            Item("Gun", 500, 350, "assets/gun.png")
        ]

    def draw_items(self, screen):
        # Sort items by z_index before drawing
        for item in sorted(self.items, key=lambda x: getattr(x, "z_index", 0)):
            item.draw_item(screen)