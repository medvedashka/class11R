import json
import csv

class Contact:
    def __init__(self, name, phone, email, contact_id=None):
        self.id = contact_id if contact_id is not None else self._generate_id()
        self.name = name
        self.phone = phone
        self.email = email

    def _generate_id(self):
        from datetime import datetime
        return int(datetime.timestamp(datetime.now()))

    def update(self, name=None, phone=None, email=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }

    @staticmethod
    def from_dict(data):
        return Contact(
            name=data['name'],
            phone=data['phone'],
            email=data['email'],
            contact_id=data['id']
        )


class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self._load_contacts()

    def _load_contacts(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                contacts_data = json.load(file)
                return [Contact.from_dict(contact) for contact in contacts_data]
        except FileNotFoundError:
            return []

    def _save_contacts(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        self._save_contacts()

    def get_all_contacts(self):
        return self.contacts

    def get_contact_by_id(self, contact_id):
        return next((contact for contact in self.contacts if contact.id == contact_id), None)

    def get_contact_by_name_or_phone(self, query):
        return [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]

    def update_contact(self, contact_id, name=None, phone=None, email=None):
        contact = self.get_contact_by_id(contact_id)
        if contact:
            contact.update(name, phone, email)
            self._save_contacts()
            return True
        return False

    def delete_contact(self, contact_id):
        contact = self.get_contact_by_id(contact_id)
        if contact:
            self.contacts.remove(contact)
            self._save_contacts()
            return True
        return False

    def import_contacts_from_csv(self, csv_filename):
        with open(csv_filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.add_contact(row['name'], row['phone'], row['email'])
            self._save_contacts()

    def export_contacts_to_csv(self, csv_filename):
        with open(csv_filename, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'name', 'phone', 'email'])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.to_dict())
