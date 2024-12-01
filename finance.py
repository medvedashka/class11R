import json
from datetime import datetime
import csv

class FinanceRecord:
    def __init__(self, amount, category, date, description, record_id=None):
        self.id = record_id if record_id is not None else self._generate_id()
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def _generate_id(self):
        return int(datetime.timestamp(datetime.now()))

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description
        }

    @staticmethod
    def from_dict(data):
        return FinanceRecord(
            amount=data['amount'],
            category=data['category'],
            date=data['date'],
            description=data['description'],
            record_id=data['id']
        )


class FinanceManager:
    def __init__(self, filename='finance.json'):
        self.filename = filename
        self.records = self._load_records()

    def _load_records(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                records_data = json.load(file)
                return [FinanceRecord.from_dict(record) for record in records_data]
        except FileNotFoundError:
            return []

    def _save_records(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([record.to_dict() for record in self.records], file, indent=4)

    def add_record(self, amount, category, date, description):
        new_record = FinanceRecord(amount, category, date, description)
        self.records.append(new_record)
        self._save_records()

    def get_all_records(self):
        return self.records

    def generate_report(self, start_date, end_date):
        start = datetime.strptime(start_date, "%d-%m-%Y")
        end = datetime.strptime(end_date, "%d-%m-%Y")
        report = [record for record in self.records if start <= datetime.strptime(record.date, "%d-%m-%Y") <= end]
        return report

    def export_records_to_csv(self, csv_filename):
        with open(csv_filename, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'amount', 'category', 'date', 'description'])
            writer.writeheader()
            for record in self.records:
                writer.writerow(record.to_dict())

    def import_records_from_csv(self, csv_filename):
        with open(csv_filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.add_record(float(row['amount']), row['category'], row['date'], row['description'])
