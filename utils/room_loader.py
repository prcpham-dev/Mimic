import json
from core.interactable.item import Item
from core.interactable.NPC import NPC
from core.room import Room
from core.obstacle import Obstacle


def load_room_from_json(path):
    with open(path, 'r') as f:
        data = json.load(f)

    room_id = data["id"]
    background_color = tuple(data.get("background_color", [0, 0, 0]))
    neighbors = data.get("neighbors", {})

    interactables = []
    for obj in data.get("interactables", []):
        obj_type = obj.get("type")
        name = obj.get("name")
        x = obj.get("x", 0)
        y = obj.get("y", 0)
        sprite = obj.get("sprite")

        if obj_type == "Item":
            item = Item(name, x, y, image_path=sprite)
            interactables.append(item)
        elif obj_type == "NPC":
            dialogue = obj.get("dialogue", "")
            npc = NPC(name, x, y, image_path=sprite, dialogue=dialogue)
            interactables.append(npc)
        else:
            print(f"[WARN] Unknown interactable type in interactables: {obj_type}")

    obstacles = []
    for obj in data.get("obstacles", []):
        obj_type = obj.get("type")
        name = obj.get("name")
        x = obj.get("x", 0)
        y = obj.get("y", 0)
        sprite = obj.get("sprite")
        if obj_type == "Obstacle":
            width = obj["width"]
            height = obj["height"]
            obstacle = Obstacle(name, x, y, width, height, image_path=sprite)
            obstacles.append(obstacle)
        else:
            print(f"[WARN] Unknown obstacle type: {obj_type}")

    return Room(room_id, background_color, neighbors, interactables, obstacles)
