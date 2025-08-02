from config import INTERACT_RANGE

def is_player_near(item, player):
    range = player.rect.inflate(INTERACT_RANGE * 2, INTERACT_RANGE * 2)
    return range.colliderect(item.rect)

def handle_interaction(background, player):
    items = background.current_room.obstacles + background.current_room.interactables
    for item in items:
        if is_player_near(item, player) and item.activated:
            item.interact(player)
            return item
