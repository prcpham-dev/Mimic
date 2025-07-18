from core.interactable.interactable import Interactable
from config import ITEM_SIZE

class Item(Interactable):
    def __init__(self, name, x, y, color, image_path=None):
        width = height = ITEM_SIZE
        super().__init__(name, x, y, width, height, color)

    def interact(self, player):
        # Swap held item if already holding one
        if player.held_item:
            player.held_item.rect.center = self.rect.center

            # Swap items
            temp = player.held_item
            player.held_item = self
            print(f'Swapped {temp.name} with {self.name}!')
        else:
            player.held_item = self
            print(f'You picked up {self.name}!')
