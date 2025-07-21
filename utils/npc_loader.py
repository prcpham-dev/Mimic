import json
import os

def load_npc_conversation(npc_name):
    path = os.path.join(f"{npc_name}")
    with open(path, "r") as f:
        data = json.load(f)
    return data
