from config import WINDOW_WIDTH, WINDOW_HEIGHT
import pygame

def get_movement_delta(player, keys):
    dx, dy = 0, 0
    if keys[pygame.K_a]:
        dx -= player.speed
        player.isLeft = True
    if keys[pygame.K_d]:
        dx += player.speed
        player.isLeft = False
    if keys[pygame.K_w]:
        dy -= player.speed
    if keys[pygame.K_s]:
        dy += player.speed
    return dx, dy

def move_and_handle_x(player, dx, background):
    size = player.size
    orig_x = player.rect.x
    player.rect.x += dx

    transitioned = False
    if player.rect.x > WINDOW_WIDTH - size:
        if background.current_room.get_neighbor("right"):
            background.transition("right", player)
            transitioned = True
        else:
            player.rect.x = WINDOW_WIDTH - size
    elif player.rect.x < 0:
        if background.current_room.get_neighbor("left"):
            background.transition("left", player)
            transitioned = True
        else:
            player.rect.x = 0

    if not transitioned:
        for obstacle in getattr(background.current_room, "obstacles", []):
            if player.rect.colliderect(obstacle.rect):
                player.rect.x = orig_x
                break

def move_and_handle_y(player, dy, background):
    size = player.size
    orig_y = player.rect.y
    player.rect.y += dy

    transitioned = False
    if player.rect.y > WINDOW_HEIGHT - size:
        if background.current_room.get_neighbor("down"):
            background.transition("down", player)
            transitioned = True
        else:
            player.rect.y = WINDOW_HEIGHT - size
    elif player.rect.y < 0:
        if background.current_room.get_neighbor("up"):
            background.transition("up", player)
            transitioned = True
        else:
            player.rect.y = 0

    if not transitioned:
        for obstacle in getattr(background.current_room, "obstacles", []):
            if player.rect.colliderect(obstacle.rect):
                player.rect.y = orig_y
                break

def handle_input(player, keys, background):
    dx, dy = get_movement_delta(player, keys)
    move_and_handle_x(player, dx, background)
    move_and_handle_y(player, dy, background)
