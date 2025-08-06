import pygame

class Interactable:
    def __init__(self, name, x, y, width, height, image_path):
        self.name = name
        self.rect = pygame.Rect(x, y, width, height)

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.original_image = self.image.copy()
        self.activated = True

    def draw_interactable(self, screen, is_left=True):
        if is_left:
            screen.blit(self.image, self.rect.topleft)
        else:
            screen.blit(pygame.transform.flip(self.image, True, False), self.rect.topleft)

    def flip_item(self, is_left):
        if is_left:
            self.image = self.original_image
        else:
            self.image = pygame.transform.flip(self.original_image, True, False)

    def interact(self, player):
        print(f"{self.name} interacted with by player.")
