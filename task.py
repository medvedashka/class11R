from datetime import datetime
import json

class Task:
    def __init__(self, title, description, task_id=None, priority="Средний", due_date=None, done=False):
        self.id = task_id if task_id is not None else self._generate_id()
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.done = done
        self.timestamp = self._current_timestamp()

    def _generate_id(self):
        return int(datetime.timestamp(datetime.now()))

    def _current_timestamp(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def update(self, title=None, description=None, priority=None, due_date=None, done=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if priority:
            self.priority = priority
        if due_date:
            self.due_date = due_date
        if done is not None:
            self.done = done
        self.timestamp = self._current_timestamp()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date,
            'done': self.done,
            'timestamp': self.timestamp
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data['title'],
            description=data['description'],
            task_id=data['id'],
            priority=data['priority'],
            due_date=data['due_date'],
            done=data['done'],
        )


class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                tasks_data = json.load(file)
                return [Task.from_dict(task) for task in tasks_data]
        except FileNotFoundError:
            return []

    def _save_tasks(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title, description, priority="Средний", due_date=None):
        new_task = Task(title, description, priority=priority, due_date=due_date)
        self.tasks.append(new_task)
        self._save_tasks()

    def get_all_tasks(self):
        return self.tasks

    def get_task_by_id(self, task_id):
        return next((task for task in self.tasks if task.id == task_id), None)

    def update_task(self, task_id, title=None, description=None, priority=None, due_date=None, done=None):
        task = self.get_task_by_id(task_id)
        if task:
            task.update(title, description, priority, due_date, done)
            self._save_tasks()
            return True
        return False

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self._save_tasks()
            return True
        return False

    def import_tasks_from_csv(self, csv_filename):
        import csv
        with open(csv_filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.add_task(row['title'], row['description'], row['priority'], row['due_date'])
            self._save_tasks()

    def export_tasks_to_csv(self, csv_filename):
        import csv
        with open(csv_filename, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'description', 'priority', 'due_date', 'done', 'timestamp'])
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task.to_dict())

