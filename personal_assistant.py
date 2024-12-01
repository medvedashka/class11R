from note import NoteManager
from task import TaskManager
from contact import ContactManager

def print_menu():
    print("Добро пожаловать в Персональный помощник!")
    print("Выберите действие:")
    print("1. Управление заметками")
    print("2. Управление задачами")
    print("3. Управление контактами")
    print("4. Выход")

def note_menu():
    print("1. Создать новую заметку")
    print("2. Просмотреть все заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Экспорт заметок в CSV")
    print("6. Импорт заметок из CSV")
    print("7. Назад")

def task_menu():
    print("1. Создать новую задачу")
    print("2. Просмотреть все задачи")
    print("3. Редактировать задачу")
    print("4. Удалить задачу")
    print("5. Экспорт задач в CSV")
    print("6. Импорт задач из CSV")
    print("7. Назад")

def contact_menu():
    print("1. Создать новый контакт")
    print("2. Просмотреть все контакты")
    print("3. Редактировать контакт")
    print("4. Удалить контакт")
    print("5. Экспорт контактов в CSV")
    print("6. Импорт контактов из CSV")
    print("7. Поиск контакта")
    print("8. Назад")

def main():
    note_manager = NoteManager()
    task_manager = TaskManager()
    contact_manager = ContactManager()

    while True:
        print_menu()
        choice = input("Ваш выбор: ")

        if choice == '1':
            while True:
                note_menu()
                note_choice = input("Ваш выбор: ")
                if note_choice == '1':
                    title = input("Введите заголовок заметки: ")
                    content = input("Введите содержимое заметки: ")
                    note_manager.add_note(title, content)
                    print("Заметка добавлена!")
                elif note_choice == '2':
                    notes = note_manager.get_all_notes()
                    if notes:
                        for note in notes:
                            print(f"ID: {note.id}, Заголовок: {note.title}, Дата: {note.timestamp}")
                    else:
                        print("Нет заметок.")
                elif note_choice == '3':
                    note_id = int(input("Введите ID заметки для редактирования: "))
                    note = note_manager.get_note_by_id(note_id)
                    if note:
                        new_title = input(f"Введите новый заголовок (старый: {note.title}): ")
                        new_content = input(f"Введите новое содержимое (старое: {note.content}): ")
                        note_manager.update_note(note_id, new_title, new_content)
                        print("Заметка обновлена!")
                    else:
                        print("Заметка не найдена.")
                elif note_choice == '4':
                    note_id = int(input("Введите ID заметки для удаления: "))
                    if note_manager.delete_note(note_id):
                        print("Заметка удалена!")
                    else:
                        print("Заметка не найдена.")
                elif note_choice == '5':
                    filename = input("Введите имя CSV файла для экспорта: ")
                    note_manager.export_notes_to_csv(filename)
                    print(f"Заметки экспортированы в {filename}")
                elif note_choice == '6':
                    filename = input("Введите имя CSV файла для импорта: ")
                    note_manager.import_notes_from_csv(filename)
                    print(f"Заметки импортированы из {filename}")
                elif note_choice == '7':
                    break
                else:
                    print("Неверный выбор. Попробуйте снова.")

        elif choice == '2':
            while True:
                task_menu()
                task_choice = input("Ваш выбор: ")
                if task_choice == '1':
                    title = input("Введите заголовок задачи: ")
                    description = input("Введите описание задачи: ")
                    priority = input("Введите приоритет задачи (Высокий/Средний/Низкий): ")
                    due_date = input("Введите срок выполнения задачи (ДД-ММ-ГГГГ): ")
                    task_manager.add_task(title, description, priority, due_date)
                    print("Задача добавлена!")
                elif task_choice == '2':
                    tasks = task_manager.get_all_tasks()
                    if tasks:
                        for task in tasks:
                            status = "Выполнена" if task.done else "Не выполнена"
                            print(f"ID: {task.id}, Заголовок: {task.title}, Приоритет: {task.priority}, Статус: {status}")
                    else:
                        print("Нет задач.")
                elif task_choice == '3':
                    task_id = int(input("Введите ID задачи для редактирования: "))
                    task = task_manager.get_task_by_id(task_id)
                    if task:
                        new_title = input(f"Введите новый заголовок (старый: {task.title}): ")
                        new_description = input(f"Введите новое описание (старое: {task.description}): ")
                        new_priority = input(f"Введите новый приоритет (старый: {task.priority}): ")
                        new_due_date = input(f"Введите новый срок выполнения (старый: {task.due_date}): ")
                        done = input(f"Задача выполнена? (Да/Нет): ").lower() == 'да'
                        task_manager.update_task(task_id, new_title, new_description, new_priority, new_due_date, done)
                        print("Задача обновлена!")
                    else:
                        print("Задача не найдена.")
                elif task_choice == '4':
                    task_id = int(input("Введите ID задачи для удаления: "))
                    if task_manager.delete_task(task_id):
                        print("Задача удалена!")
                    else:
                        print("Задача не найдена.")
                elif task_choice == '5':
                    filename = input("Введите имя CSV файла для экспорта: ")
                    task_manager.export_tasks_to_csv(filename)
                    print(f"Задачи экспортированы в {filename}")
                elif task_choice == '6':
                    filename = input("Введите имя CSV файла для импорта: ")
                    task_manager.import_tasks_from_csv(filename)
                    print(f"Задачи импортированы из {filename}")
                elif task_choice == '7':
                    break
                else:
                    print("Неверный выбор. Попробуйте снова.")

        if choice == '3':
            while True:
                contact_menu()
                contact_choice = input("Ваш выбор: ")

                if contact_choice == '1':
                    name = input("Введите имя контакта: ")
                    phone = input("Введите номер телефона: ")
                    email = input("Введите email: ")
                    contact_manager.add_contact(name, phone, email)
                    print("Контакт добавлен!")

                elif contact_choice == '2':
                    contacts = contact_manager.get_all_contacts()
                    if contacts:
                        for contact in contacts:
                            print(f"ID: {contact.id}, Имя: {contact.name}, Телефон: {contact.phone}, Email: {contact.email}")
                    else:
                        print("Нет контактов.")

                elif contact_choice == '3':
                    contact_id = int(input("Введите ID контакта для редактирования: "))
                    contact = contact_manager.get_contact_by_id(contact_id)
                    if contact:
                        new_name = input(f"Введите новое имя (старое: {contact.name}): ")
                        new_phone = input(f"Введите новый номер телефона (старое: {contact.phone}): ")
                        new_email = input(f"Введите новый email (старый: {contact.email}): ")
                        contact_manager.update_contact(contact_id, new_name, new_phone, new_email)
                        print("Контакт обновлён!")
                    else:
                        print("Контакт не найден.")

                elif contact_choice == '4':
                    contact_id = int(input("Введите ID контакта для удаления: "))
                    if contact_manager.delete_contact(contact_id):
                        print("Контакт удалён!")
                    else:
                        print("Контакт не найден.")

                elif contact_choice == '5':
                    filename = input("Введите имя CSV файла для экспорта: ")
                    contact_manager.export_contacts_to_csv(filename)
                    print(f"Контакты экспортированы в {filename}")

                elif contact_choice == '6':
                    filename = input("Введите имя CSV файла для импорта: ")
                    contact_manager.import_contacts_from_csv(filename)
                    print(f"Контакты импортированы из {filename}")

                elif contact_choice == '7':
                    query = input("Введите имя или номер телефона для поиска: ")
                    results = contact_manager.get_contact_by_name_or_phone(query)
                    if results:
                        for contact in results:
                            print(f"ID: {contact.id}, Имя: {contact.name}, Телефон: {contact.phone}, Email: {contact.email}")
                    else:
                        print("Контакты не найдены.")

                elif contact_choice == '8':
                    break
                else:
                    print("Неверный выбор. Попробуйте снова.")
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()