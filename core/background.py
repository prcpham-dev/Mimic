import pygame
import config

class Background:
    def __init__(self):
        self.color = config.BACKGROUND_COLOR

    def draw_background(self, screen):
        screen.fill((0, 0, 0))

