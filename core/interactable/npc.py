from core.interactable.interactable import Interactable
from config import NPC_SIZE

class NPC(Interactable):
    def __init__(self, name, x, y, image_path, dialogue):
        width = height = NPC_SIZE
        super().__init__(name, x, y, width, height, image_path)
        self.dialogue = dialogue

    def interact(self, player):
        print(f"{self.name}: {self.dialogue}")
