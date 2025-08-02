import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT

class BaseTask:
    def __init__(self, name, background_img=None):
        self.name = name
        self.completed = False
        self.success = False
        self.background_img = background_img

    def start(self):
        self.completed = False
        self.success = False

    def draw_screen(self, screen):
        if self.background_img:
            img = pygame.image.load(self.background_img)
            img = pygame.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))
            screen.blit(img, (0, 0))
        else:
            screen.fill((20, 20, 20))

    def run(self, events):
        pass

    def on_task_completed(self):
        pass
