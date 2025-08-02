import pygame
from core.tasks.task import BaseTask

class PlantingTask(BaseTask):
    def __init__(self):
        super().__init__("Planting", background_img="assets/background/tasks/plantGame.png")
        self.progress = 0
        self.font = pygame.font.SysFont(None, 36)


    def run(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.progress += 1
                if self.progress >= 5:
                    self.completed = True
                    self.success = True

    def draw_screen(self, screen):
        super().draw_screen(screen)
        text = self.font.render(f"Planting (press space)... {self.progress}/5", True, (255, 255, 255))
        screen.blit(text, (100, 100))

    def on_task_completed(self):
        print("[Planting] Task completed!")