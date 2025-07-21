from core.interactable.interactable import Interactable
import pygame

class Obstacle(Interactable):
    def __init__(self, name, x, y, width, height, image_path):
        super().__init__(name, x, y, width, height, image_path)
    