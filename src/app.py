class Task:
    def __init__(self, title, description="", priority="normal"):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description="", priority="normal"):
        if not title:
            raise ValueError("O título é obrigatório")
        task = Task(title, description, priority)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def update_task(self, index, title=None, description=None, priority=None):
        task = self.tasks[index]
        if title:
            task.title = title
        if description:
            task.description = description
        if priority:
            task.priority = priority
        return task

    def delete_task(self, index):
        self.tasks.pop(index)

    def list_tasks(self):
        return self.tasks
