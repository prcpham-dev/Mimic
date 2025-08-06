from core.interactable.obstacle import Obstacle
from core.tasks.planting_task import PlantingTask

class Garden_plot(Obstacle):
    def __init__(self, name, x, y, width, height, image_path):
        super().__init__(name, x, y, width, height, image_path)

    def interact(self, game):
        game.task_manager.start_task(PlantingTask())