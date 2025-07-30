import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT

class BaseTask:
    def __init__(self, name, minigame_bg_color=(20, 20, 20)):
        self.name = name
        self.completed = False
        self.success = False
        self.minigame_bg_color = minigame_bg_color

    def start(self):
        self.completed = False
        self.success = False

    def draw_screen(self, screen):
        screen.fill(self.minigame_bg_color)
        
    def run(self, events):
        pass

    def on_task_completed(self):
        pass
