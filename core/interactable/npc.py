from core.interactable.interactable import Interactable
from utils.npc_loader import load_npc_conversation
from config import NPC_SIZE

class NPC(Interactable):
    def __init__(self, name, x, y, image_path, dialog_path):
        width = height = NPC_SIZE
        self.dialog_path = dialog_path
        super().__init__(name, x, y, width, height, image_path )

    def interact(self, player):
        conversation = load_npc_conversation(self.dialog_path)
        player.dialog.open(self.name, conversation)