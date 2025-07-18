from core.interactable.interactable import Interactable
from config import ITEM_SIZE

class Item(Interactable):
    def __init__(self, name, x, y, image_path=None, activated=True):
        width = height = ITEM_SIZE
        self.activated = activated
        super().__init__(name, x, y, width, height, image_path)

    def interact(self, player):
        if not self.activated:
            return

        if player.held_item:
            player.held_item.activated = True
            player.held_item.z_index = 0
            player.held_item.rect.center = self.rect.center

        player.held_item = self
        self.activated = False

