class TaskManager:
    def __init__(self):
        self.current_task = None

    def start_task(self, task):
        self.current_task = task
        self.current_task.start()

    def stop_task(self):
        self.current_task = None

    def is_running(self):
        return self.current_task is not None

    def run(self, events):
        if self.current_task:
            self.current_task.run(events)
            if self.current_task.completed:
                self.current_task.on_task_completed()
                self.stop_task()

    def draw(self, screen):
        if self.current_task:
            self.current_task.draw_screen(screen)
