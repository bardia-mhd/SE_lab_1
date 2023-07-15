class TaskManager:
    def __init__(self, db_path='./db/tasks.json'):
        self.db_path = db_path
        if os.path.exists(db_path):
            with open(db_path, 'r') as f:
                self.tasks = [Task(x['title']) if not x['done'] else (t:=Task(x['title'])).mark_done() or t for x in json.load(f)]
        else:
            if not os.path.exists('./db'):
                os.makedirs('./db')
            with open(db_path, 'w') as f:
                json.dump([], f)
            self.tasks = []
    
    def add(self, title):
        pass

    def delete(self, index):
        pass

    def mark_done(self, index):
        pass

    def list_tasks(self):
        pass

    def clear(self):
        pass
    