class Game:
    def __init__(self):
        self.dialog = None
        self.task_manager = None
        self.background = None
        self.player = None

    def set_player(self, player):
        self.player = player

    def set_dialog(self, dialog):
        self.dialog = dialog

    def set_task_manager(self, task_manager):
        self.task_manager = task_manager

    def set_background(self, background):
        self.background = background