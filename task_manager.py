class TaskManager:
    def __init__(self, db_path="./db/tasks.json"):
        self.db_path = db_path
        if os.path.exists(db_path):
            with open(db_path, "r") as f:
                self.tasks = [
                    Task(x["title"])
                    if not x["done"]
                    else (t := Task(x["title"])).mark_done() or t
                    for x in json.load(f)
                ]
        else:
            if not os.path.exists("./db"):
                os.makedirs("./db")
            with open(db_path, "w") as f:
                json.dump([], f)
            self.tasks = []

    def save_to_db(self):
        with open(self.db_path, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def add(self, title):
        task = Task(title)
        self.tasks.append(task)
        self.save_to_db()

    def delete(self, index):
        if index < len(self.tasks):
            del self.tasks[index]
            self.save_to_db()

    def mark_done(self, index):
        if index < len(self.tasks):
            self.tasks[index].mark_done()
            self.save_to_db()

    def list_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index}: {task}")

    def clear(self):
        self.tasks = []
        self.save_to_db()

    def __str__(self):
        return "1"