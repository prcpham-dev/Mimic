import pygame

class Interactable:
    def __init__(self, name, x, y, width, height, image_path):
        self.name = name
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.activated = True

    def draw_item(self, screen, isLeft=True):
        if isLeft:
            screen.blit(self.image, self.rect.topleft)
        else:
            screen.blit(pygame.transform.flip(self.image, True, False), self.rect.topleft)

    def interact(self, player):
        raise NotImplementedError("Subclasses must implement 'interact()'")
