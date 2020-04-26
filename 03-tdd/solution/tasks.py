import datetime


class Task:
    def __init__(self, title, date=None):
        self.title = title
        if date is None:
            self.date = datetime.date.today()
        else:
            self.date = date


class Tasks:
    def __init__(self):
        self.tasks = []

    def add_task(self, new_task):
        assert isinstance(new_task, Task)
        self.tasks.append(new_task)

    def done(self, task):
        assert isinstance(task, Task)
        if task in self.tasks:
            self.tasks.remove(task)

    def today(self):
        """Today returns a list of today's tasks"""
        return [t for t in self.tasks if t.date == datetime.date.today()]

    def tomorrow(self):
        """Today returns a list of tomorrow's tasks"""
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        return [t for t in self.tasks if t.date == tomorrow]
