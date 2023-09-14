# Функция для сохранения заметок в файл
def save_notes():
    with open("notes.json", "w") as f:
        notes_data = []
        for note in notes_manager.notes:
            note_data = {
                "id": note.id,
                "title": note.title,
                "body": note.body,
                "date": note.date
            }
            notes_data.append(note_data)
        json.dump(notes_data, f)
