import json
from note import Note, NoteManager


def print_menu():
    print("Добро пожаловать в Персональный помощник!")
    print("Выберите действие:")
    print("1. Управление заметками")
    print("2. Выход")

def note_menu():
    print("1. Создать новую заметку")
    print("2. Просмотреть все заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Экспорт заметок в CSV")
    print("6. Импорт заметок из CSV")
    print("7. Назад")

def main():
    note_manager = NoteManager()
    
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
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
