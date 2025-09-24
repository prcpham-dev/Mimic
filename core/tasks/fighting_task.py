import pygame
from core.tasks.task import BaseTask

class FightingTask(BaseTask):
    def __init__(self):
        super().__init__("Fighting", background_img=None)
        self.font = pygame.font.SysFont(None, 36)