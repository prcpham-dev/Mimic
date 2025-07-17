from core.interactable.interactable import Interactable

class ItemInteract(Interactable):
    def interact(self, player):
        print("You picked up an item!")