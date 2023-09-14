# Функция для вывода списка заметок
# Функция для вывода списка заметок
def print_notes(notes):
    if not notes:
        print("Заметок не найдено.")
    else:
        for note in notes:
            date_str = datetime.fromtimestamp(note.date).strftime("%d.%m.%Y %H:%M:%S")
            print(f"{note.id}. {note.title} ({date_str})")