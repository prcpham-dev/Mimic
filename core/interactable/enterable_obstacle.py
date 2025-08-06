from core.interactable.obstacle import Obstacle

class EnterableObstacle(Obstacle):
    def __init__(self, name, x, y, width, height, image_path, 
                 target_room=None, spawn_position=None, interaction_side="bottom"):
        super().__init__(name, x, y, width, height, image_path)
        
        self.target_room = target_room
        self.spawn_position = spawn_position
        self.interaction_side = interaction_side

    def is_player_facing(self, player):
        buffer = 10
        if self.interaction_side == "top":
            return (player.rect.bottom >= self.rect.top - buffer and 
                    player.rect.bottom <= self.rect.top + buffer and
                    player.rect.centerx in range(self.rect.left, self.rect.right))
        elif self.interaction_side == "bottom":
            return (player.rect.top <= self.rect.bottom + buffer and 
                    player.rect.top >= self.rect.bottom - buffer and
                    player.rect.centerx in range(self.rect.left, self.rect.right))
        elif self.interaction_side == "left":
            return (player.rect.right >= self.rect.left - buffer and 
                    player.rect.right <= self.rect.left + buffer and
                    player.rect.centery in range(self.rect.top, self.rect.bottom))
        elif self.interaction_side == "right":
            return (player.rect.left <= self.rect.right + buffer and 
                    player.rect.left >= self.rect.right - buffer and
                    player.rect.centery in range(self.rect.top, self.rect.bottom))
        return False

    def interact(self, game):
        player = game.player
        background = game.background
        
        if self.target_room and self.is_player_facing(player):
            background.current_room = background._load_room(self.target_room)
            if self.spawn_position:
                player.rect.topleft = self.spawn_position
