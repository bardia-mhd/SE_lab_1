class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        return f"{self.title} - {'Done' if self.done else 'Not done'}"

    def to_dict(self):
        return {"title": self.title, "done": self.done}
