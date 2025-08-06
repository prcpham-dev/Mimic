from core.interactable.obstacle import Obstacle

class EnterableObstacle(Obstacle):
    def __init__(self, name, x, y, width, height, image_path, interaction_direction=None):
        super().__init__(name, x, y, width, height, image_path, interaction_direction)

    def interact(self, game):
        if self.interaction_direction:
            game.background.transition(self.interaction_direction, game.player)
