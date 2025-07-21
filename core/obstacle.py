import pygame

class Obstacle:
    def __init__(self, name, x, y, width, height, image_path):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw_obstacle(self, screen):
        screen.blit(self.image, self.rect)