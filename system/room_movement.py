from config import WINDOW_WIDTH, WINDOW_HEIGHT

def handle_room_transition_or_clamp(player, background):
    size = player.size
    
    # RIGHT
    if player.rect.x > WINDOW_WIDTH - size:
        if background.current_room.get_neighbor("right"):
            background.transition("right", player)
        else:
            player.rect.x = WINDOW_WIDTH - size

    # LEFT
    if player.rect.x < 0:
        if background.current_room.get_neighbor("left"):
            background.transition("left", player)
        else:
            player.rect.x = 0

    # DOWN
    if player.rect.y > WINDOW_HEIGHT - size:
        if background.current_room.get_neighbor("down"):
            background.transition("down", player)
        else:
            player.rect.y = WINDOW_HEIGHT - size

    # UP
    if player.rect.y < 0:
        if background.current_room.get_neighbor("up"):
            background.transition("up", player)
        else:
            player.rect.y = 0
