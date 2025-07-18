from core.interactable.interactable import Interactable
from config import NPC_SIZE

class npc(Interactable):
    def __init__(self, name, x, y, color, dialogue):
        width = height = NPC_SIZE
        super().__init__(name, x, y, width, height, color)
        self.dialogue = dialogue

    def interact(self, player):
        print(f"{self.name}: {self.dialogue}")
