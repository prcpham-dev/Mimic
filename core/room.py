class Room:
    def __init__(self, room_id, background_color, neighbors=None, interactables=None):
        self.room_id = room_id
        self.background_color = background_color
        self.neighbors = neighbors or {"up": None, "down": None, "left": None, "right": None}
        self.interactables = interactables or []

    def get_neighbor(self, direction):
        return self.neighbors.get(direction)

    def add_interactable(self, obj):
        self.interactables.append(obj)