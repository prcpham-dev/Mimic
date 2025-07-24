from core.interactable.interactable import Interactable
import pygame

class Obstacle(Interactable):
    def __init__(self, name, x, y, width, height, image_path):
        super().__init__(name, x, y, width, height, image_path)
        self.image_path = image_path

    def draw_interactable(self, screen, isLeft=True):
        if not self.image_path:
            return
        super().draw_interactable(screen, isLeft)
