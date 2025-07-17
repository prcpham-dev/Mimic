import pygame

class Interactable:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.activated = True

    def draw_item(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
    def interact(self, player):
        raise NotImplementedError("Subclasses must implement 'interact()'")