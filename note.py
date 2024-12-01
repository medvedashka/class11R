from datetime import datetime
import json

class Note:
    def __init__(self, title, content, note_id=None, timestamp=None):
        self.id = note_id if note_id is not None else self._generate_id()
        self.title = title
        self.content = content
        self.timestamp = timestamp if timestamp else self._current_timestamp()

    def _generate_id(self):
        return int(datetime.timestamp(datetime.now()))

    def _current_timestamp(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def update(self, title=None, content=None):
        if title:
            self.title = title
        if content:
            self.content = content
        self.timestamp = self._current_timestamp()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'timestamp': self.timestamp
        }

    @staticmethod
    def from_dict(data):
        return Note(
            title=data['title'],
            content=data['content'],
            note_id=data['id'],
            timestamp=data['timestamp']
        )


class NoteManager:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = self._load_notes()

    def _load_notes(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                notes_data = json.load(file)
                return [Note.from_dict(note) for note in notes_data]
        except FileNotFoundError:
            return []

    def _save_notes(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([note.to_dict() for note in self.notes], file, indent=4)

    def add_note(self, title, content):
        new_note = Note(title, content)
        self.notes.append(new_note)
        self._save_notes()

    def get_all_notes(self):
        return self.notes

    def get_note_by_id(self, note_id):
        return next((note for note in self.notes if note.id == note_id), None)

    def update_note(self, note_id, title=None, content=None):
        note = self.get_note_by_id(note_id)
        if note:
            note.update(title, content)
            self._save_notes()
            return True
        return False

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self._save_notes()
            return True
        return False

    def import_notes_from_csv(self, csv_filename):
        import csv
        with open(csv_filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.add_note(row['title'], row['content'])
            self._save_notes()

    def export_notes_to_csv(self, csv_filename):
        import csv
        with open(csv_filename, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'content', 'timestamp'])
            writer.writeheader()
            for note in self.notes:
                writer.writerow(note.to_dict())
