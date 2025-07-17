from core.interactable.interactable import Interactable

class npc(Interactable):
    def __init__(self, x, y, width, height, color, name, dialogue):
        super().__init__(x, y, width, height, color)
        self.name = name
        self.dialogue = dialogue

    def interact(self, player):
        print(f"{self.name}: {self.dialogue}")
