from config import INTERACT_RANGE

def is_player_near(item, player):
    range = player.rect.inflate(INTERACT_RANGE * 2, INTERACT_RANGE * 2)
    return range.colliderect(item.rect)

def handle_interaction(game):
    items = game.background.current_room.obstacles + game.background.current_room.interactables
    for item in items:
        if is_player_near(item, game.player) and item.activated:
            item.interact(game)
            break
