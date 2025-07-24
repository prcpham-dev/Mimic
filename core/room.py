class Room:
    def __init__(self, room_id, background_img, neighbors=None, interactables=None, obstacles=None):
        self.room_id = room_id
        self.background_img = background_img
        self.neighbors = neighbors or {"up": None, "down": None, "left": None, "right": None}
        self.interactables = interactables or []
        self.obstacles = obstacles or []

    def get_neighbor(self, direction):
        return self.neighbors.get(direction)

    def add_interactable(self, obj):
        self.interactables.append(obj)

    def add_obstacle(self, obj):
        self.obstacles.append(obj)
