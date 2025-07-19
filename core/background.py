from utils.room_loader import load_room_from_json
from config import WINDOW_WIDTH, WINDOW_HEIGHT

class Background:
    def __init__(self):
        self.rooms = {}
        self.current_room = self._load_room("room_1")

    def _load_room(self, room_id):
        if room_id not in self.rooms:
            path = f"data/rooms/{room_id}.json"
            self.rooms[room_id] = load_room_from_json(path)
        return self.rooms[room_id]

    def transition(self, direction, player):
        next_room_id = self.current_room.get_neighbor(direction)
        if next_room_id:
            self.current_room = self._load_room(next_room_id)
            self._adjust_player_position_on_transition(direction, player)

    def _adjust_player_position_on_transition(self, direction, player):
        if direction == "right":
            player.rect.x = 0
        elif direction == "left":
            player.rect.x = WINDOW_WIDTH - player.rect.width
        elif direction == "up":
            player.rect.y = WINDOW_HEIGHT - player.rect.height
        elif direction == "down":
            player.rect.y = 0

    def draw_background(self, screen):
        screen.fill(self.current_room.background_color)
        for obj in sorted(self.current_room.interactables, key=lambda x: getattr(x, "z_index", 0)):
            obj.draw_item(screen)
