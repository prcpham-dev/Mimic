# Mirror: Development Roadmap

**MirrorMind** is a pixel-art psychological sim where the player completes daily chores — but behind the scenes, the game observes, learns, and gradually mimics the player's behavior until control is lost to an AI that becomes you.

This document outlines the 15-day solo development plan.

---

## 📁 Project Structure

```
pixel_ai_game/
│
├── main.py                    # Entry point, game loop
├── config.py                  # Global constants (screen size, FPS, etc.)
│
├── assets/                    # Art, audio, fonts
│   ├── player.png
│   ├── npc.png
│   ├── font.ttf
│   └── ...
│
├── core/                      # Game components (player, npc, tasks, UI)
│   ├── player.py              # Player movement + control
│   ├── npc.py                 # Static NPC behavior
│   ├── task.py                # Chore/task system
│   └── ui.py                  # Timer, prediction bar, overlays
│
├── system/                    # AI behavior engine
│   ├── logger.py              # Logs player actions to JSON
│   ├── predictor.py           # Predicts actions, calculates accuracy
│   └── ghost_engine.py        # Controls ghosting behavior based on accuracy
│
├── utils/                     # General-purpose utilities
│   ├── file_io.py             # JSON read/write helpers
│   └── timer.py               # In-game countdown timer logic
│
├── data/                      # Saved logs and player behavior data
│   ├── day_1.json
│   ├── day_2.json
│   └── ...
│
└── README.md                  # Project description and how to run
```

---

## 🗓️ 15-Day Development Plan

// ...existing code...** is a pixel-art psychological sim where the player completes daily chores — but behind the scenes, the game observes, learns, and gradually mimics the player's behavior until control is lost to an AI that becomes you.

This document outlines the 15-day solo development plan.

---

## 🗓️ 15-Day Development Plan

### Day 1: Project Setup and Player Movement
- Set up folder structure and install Pygame
- Create game window and main loop
- Add a simple player object that can move around
- Prevent the player from leaving the screen

### Day 2: Interactable System (Tasks & NPCs)
- Create a base `Interactable` class
- Add `ItemInteract` (task) and `NPC` (dialogue) subclasses
- Enable `E` key interaction when the player is near
- Add basic tasks and NPCs to the game world

### Day 3: Logger System
- Create `logger.py` to track:
  - Task order and completion
  - Interactions with NPCs
  - Time per action
- Save data to JSON files in a `data/` folder

### Day 4: Day Timer System
- Add a visible countdown timer (5–8 minutes per day)
- End the game day automatically when time runs out
- Optionally show a summary screen

### Day 5: Room Transition System
- Create a `Room` class with neighbors (`up`, `down`, `left`, `right`)
- Handle transitions when the player touches the screen edges
- Load new rooms and adjust player position accordingly

### Day 6: Item Holding and Swapping
- Allow the player to hold one item at a time
- Picking up a new item drops the current one back into the world
- Visually draw held item beside the player (left/right side)

### Day 7: More Task Variety
- Add multiple types of interactable tasks
- Introduce mistakes the player must correct (e.g. wrong order)
- Log task behavior for learning

### Day 8: Prediction Engine (v1)
- Build a basic prediction engine (frequency-based)
- Before each task, guess what the player will do
- Track and store predictions vs actual behavior

### Day 9: Accuracy Evaluation
- Calculate prediction accuracy each day
- Save and display a confidence score (0–100%)
- Feed score into the ghost control engine

### Day 10: Ghost Control (Phase 1)
- When accuracy > 60%, begin light ghosting:
  - Slight input override
  - Pre-movement before player acts
- Reflect this subtly in the UI or behavior

### Day 11: Ghost Control (Phase 2)
- At 90%+, allow the AI to override key decisions
- Lock out the player from certain tasks
- Have the AI complete chores on your behalf

### Day 12: Dialogue Memory
- NPCs remember past conversations
- Begin echoing player tone, word choice, or task logic
- Start shifting from helpers to reflections

### Day 13: Dynamic AI Behavior
- Adjust predictions and ghosting based on evolving habits
- Add variety to ghost actions
- Simulate a learning model that adapts over time

### Day 14: Emotion and Style Mimicry
- Track player tendencies (e.g. kindness, selfishness, efficiency)
- Mirror those patterns in the AI and NPC dialogue
- Create eerie moments of recognition

### Day 15: Polish and Save System
- Add save/load support for behavior history
- Final UI polish and bug cleanup
- Test with multiple users for personalization

